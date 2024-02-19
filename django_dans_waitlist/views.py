from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers.waitlist import WaitlistEntrySerializer
from .permissions import AdminOnly
from .regex import REGEX_EMAIL
from .models import WaitlistEntry
from django.conf import settings
from django_dans_notifications.models.email import NotificationEmail
from rest_framework import status
import re
from .api_response_handler import ApiResponseHandler


# =============================== #
#
# WAITLIST ENTRY VIEW SET
#
class WaitlistEntryViewSet(viewsets.GenericViewSet):
    model = WaitlistEntry
    response_handler = ApiResponseHandler()
    queryset = WaitlistEntry.objects.all()
    serializer_class = WaitlistEntrySerializer
    permission_classes = (AllowAny,)

    def create(self, request: Request) -> Response:
        """
        Endpoint to CREATE a waitlist entry.

        Required fields:
        - email (str): The email of the user to add to the waitlist.
        """
        if not re.match(REGEX_EMAIL, request.data.get("email", "")):
            return self.response_handler.response_error(
                error_fields={"email": ["Invalid email format."]}
            )

        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return self.response_handler.response_success(
                message="Added to the waitlist.", results=serializer.data
            )
        except (ValidationError, DRFValidationError, IntegrityError) as e:
            return self.response_handler.response_error(
                error=e, error_fields=serializer.errors
            )


# =============================== #
#
# WAITLIST ENTRIES EMAIL VIEW SET
#
class WaitlistEntryEmailViewSet(viewsets.GenericViewSet):
    response_handler = ApiResponseHandler()
    queryset = WaitlistEntry.objects.all()
    permission_classes = (AdminOnly,)

    def create(self, request: Request) -> Response:
        """
        Endpoint to CREATE a mass email to the waitlist.

        Required fields:
        - message (str): The message to send to the waitlist.

        Optional fields:
        - subject (str): The subject of the email.
        """
        message = request.data.get("message", "")
        subject = request.data.get("subject", None)

        if message == "":
            return self.response_handler.response_error(
                error_fields={"message": ["'Message' cannot be blank or missing."]}
            )

        team_name = hasattr(settings, "TEAM_NAME")
        if subject is None or subject == "None":
            if team_name:
                subject = f"Waitlist Update from {settings.TEAM_NAME}"
            else:
                subject = "Waitlist Update from the Team"

        # get all emails
        waitlist_emails_list = []
        for waitlist_entry in WaitlistEntry.objects.all():
            waitlist_emails_list.append(waitlist_entry.email)

        # create context
        context = {"message": message}

        # add team name to context
        if team_name and context:
            if "team_name" not in context:
                context["team_name"] = settings.TEAM_NAME
        # send email
        notification_email = NotificationEmail.objects.send_email(
            subject=subject,
            template="emails/waitlist-email.html",
            sender=settings.DEFAULT_FROM_EMAIL,
            recipients=waitlist_emails_list,
            context=context,
        )

        if not notification_email.sent_successfully:
            return self.response_handler.response_error(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message="Error sending email. Please try again later.",
            )

        return self.response_handler.response_success(
            message="Successfully sent message(s)!"
        )
