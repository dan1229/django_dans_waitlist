import json
from ..base import BaseAPITestCase
from ....views import WaitlistEntryEmailViewSet
from ....models import WaitlistEntry
from django.contrib.auth import get_user_model
from django_dans_notifications.models.email import NotificationEmail

"""
# =============================================================================================
# TEST WAITLIST ENTRY EMAIL VIEW SET ==========================================================
# =============================================================================================
"""


class TestWaitlistEntryEmailViewSet(BaseAPITestCase):
    def setUp(self) -> None:
        super(TestWaitlistEntryEmailViewSet, self).setUp()
        self.view_create = WaitlistEntryEmailViewSet.as_view({"post": "create"})

        # create admin user
        self.admin_user = get_user_model().objects.create(
            username="admin",
            email="email@email.com",
            password="password",
            is_staff=True,
        )

    @staticmethod
    def get_url() -> str:
        return "/api/waitlist/entries/emails"

    # ==================================================================================
    # CREATE ===========================================================================
    # ==================================================================================

    # unauthorized
    def test_unauthorized_not_logged_in(self) -> None:
        form_data = {
            "message": "Test message",
        }
        request = self.factory.post(
            self.get_url(),
            data=form_data,
        )
        response = self.view_create(request)
        response.render()  # type: ignore[attr-defined]

        # confirm status code and data
        self.assertEqual(response.status_code, 401)

    # unauthorized
    def test_unauthorized_not_admin(self) -> None:
        form_data = {
            "message": "Test message",
        }
        request = self.factory.post(
            self.get_url(),
            HTTP_AUTHORIZATION=self.get_headers(self.user),
            data=form_data,
        )
        response = self.view_create(request)
        response.render()  # type: ignore[attr-defined]
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            json_response["detail"],
            "You do not have permission to perform this action.",
        )

    # missing subject
    def test_create_missing_subject(self) -> None:
        form_data = {
            "message": "Test message",
        }
        request = self.factory.post(
            self.get_url(),
            HTTP_AUTHORIZATION=self.get_headers(self.admin_user),
            data=form_data,
        )
        response = self.view_create(request)
        response.render()  # type: ignore[attr-defined]
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response["message"], "Successfully sent message(s)!")

    # empty subject
    def test_create_empty_subject(self) -> None:
        form_data = {
            "subject": "",
            "message": "Test message",
        }
        request = self.factory.post(
            self.get_url(),
            HTTP_AUTHORIZATION=self.get_headers(self.admin_user),
            data=form_data,
        )
        response = self.view_create(request)
        response.render()  # type: ignore[attr-defined]
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response["message"], "Successfully sent message(s)!")

    # missing message
    def test_create_missing_message(self) -> None:
        form_data = {
            "subject": "Test subject",
        }
        request = self.factory.post(
            self.get_url(),
            HTTP_AUTHORIZATION=self.get_headers(self.admin_user),
            data=form_data,
        )
        response = self.view_create(request)
        response.render()  # type: ignore[attr-defined]
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json_response["message"], "'Message' cannot be blank or missing."
        )
        self.assertEqual(
            json_response["error_fields"]["message"][0],
            "'Message' cannot be blank or missing.",
        )

    # empty message
    def test_create_empty_message(self) -> None:
        form_data = {
            "subject": "Test subject",
            "message": "",
        }
        request = self.factory.post(
            self.get_url(),
            HTTP_AUTHORIZATION=self.get_headers(self.admin_user),
            data=form_data,
        )
        response = self.view_create(request)
        response.render()  # type: ignore[attr-defined]
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json_response["message"], "'Message' cannot be blank or missing."
        )
        self.assertEqual(
            json_response["error_fields"]["message"][0],
            "'Message' cannot be blank or missing.",
        )

    # no waitlist entries
    def test_create_no_waitlist_entries(self) -> None:
        form_data = {
            "subject": "Test subject",
            "message": "Test message",
        }
        request = self.factory.post(
            self.get_url(),
            HTTP_AUTHORIZATION=self.get_headers(self.admin_user),
            data=form_data,
        )
        response = self.view_create(request)
        response.render()  # type: ignore[attr-defined]
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response["message"], "Successfully sent message(s)!")
        self.assertEqual(NotificationEmail.objects.count(), 1)
        self.assertEqual(NotificationEmail.objects.first().recipients, "")

    # one waitlist entry
    def test_create_one_waitlist_entry(self) -> None:
        # Create a waitlist entry for testing
        email1 = "test@example.com"
        WaitlistEntry.objects.create(email=email1)

        form_data = {
            "subject": "Test subject",
            "message": "Test message",
        }
        request = self.factory.post(
            self.get_url(),
            HTTP_AUTHORIZATION=self.get_headers(self.admin_user),
            data=form_data,
        )
        response = self.view_create(request)
        response.render()  # type: ignore[attr-defined]
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response["message"], "Successfully sent message(s)!")
        self.assertEqual(NotificationEmail.objects.count(), 1)
        self.assertIn(
            email1,
            NotificationEmail.objects.first().recipients,
        )

    # multiple waitlist entries
    def test_create_multiple_waitlist_entries(self) -> None:
        # Create multiple waitlist entries for testing
        email1 = "test1@example.com"
        email2 = "test2@example.com"
        email3 = "test3@example.com"
        WaitlistEntry.objects.create(email=email1)
        WaitlistEntry.objects.create(email=email2)
        WaitlistEntry.objects.create(email=email3)

        form_data = {
            "subject": "Test subject",
            "message": "Test message",
        }
        request = self.factory.post(
            self.get_url(),
            HTTP_AUTHORIZATION=self.get_headers(self.admin_user),
            data=form_data,
        )
        response = self.view_create(request)
        response.render()  # type: ignore[attr-defined]
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response["message"], "Successfully sent message(s)!")
        self.assertEqual(NotificationEmail.objects.count(), 1)
        self.assertIn(
            email1,
            NotificationEmail.objects.first().recipients,
        )
        self.assertIn(
            email2,
            NotificationEmail.objects.first().recipients,
        )
        self.assertIn(
            email3,
            NotificationEmail.objects.first().recipients,
        )
