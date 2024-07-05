import json

from ..base import BaseAPITestCase
from ....views import WaitlistEntryViewSet
from ....models import WaitlistEntry

"""
# =============================================================================================
# TEST WAITLIST ENTRY VIEW SET ================================================================
# =============================================================================================
"""


class TestWaitlistEntryViewSet(BaseAPITestCase):
    def setUp(self) -> None:
        super(TestWaitlistEntryViewSet, self).setUp()
        self.view_create = WaitlistEntryViewSet.as_view({"post": "create"})

    @staticmethod
    def get_url() -> str:
        return "/api/waitlist/entries/"

    # ==================================================================================
    # CREATE ===========================================================================
    # ==================================================================================

    def test_create_waitlist_entry_invalid_already_exists(self) -> None:
        # parameters
        email = "waitlistentry@example.com"
        form_data = {"email": email}

        # create waitlist entry
        WaitlistEntry.objects.create(email=email)

        # make api request
        request = self.factory.post(self.get_url(), data=form_data)
        response = self.view_create(request)
        response.render()
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json_response["error_fields"]["email"][0],
            "Waitlist Entry with this email already exists.",
        )
        self.assertEqual(json_response["message"], "Error. Please try again later.")

    def test_create_waitlist_entry_invalid_email(self) -> None:
        # parameters
        email = "invalidemail"
        form_data = {"email": email}

        # make api request
        request = self.factory.post(self.get_url(), data=form_data)
        response = self.view_create(request)
        response.render()
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json_response["error_fields"]["email"][0],
            "Invalid email format.",
        )
        self.assertEqual(json_response["message"], "Error. Please try again later.")

    def test_create_waitlist_entry_valid(self) -> None:
        # parameters
        email = "waitlistentry@example.com"
        form_data = {"email": email}

        # make api request
        request = self.factory.post(self.get_url(), data=form_data)
        response = self.view_create(request)
        response.render()
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json_response["message"], "Added to the waitlist.")
        self.assertEqual(json_response["results"]["email"], email)

    def test_create_waitlist_entry_missing_email(self) -> None:
        # parameters
        form_data = {}

        # make api request
        request = self.factory.post(self.get_url(), data=form_data)
        response = self.view_create(request)
        response.render()
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json_response["error_fields"]["email"][0],
            "This field is required.",
        )
        self.assertEqual(json_response["message"], "Error. Please try again later.")

    def test_create_waitlist_entry_empty_email(self) -> None:
        # parameters
        form_data = {"email": ""}

        # make api request
        request = self.factory.post(self.get_url(), data=form_data)
        response = self.view_create(request)
        response.render()
        json_response = json.loads(response.content)

        # confirm status code and data
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json_response["error_fields"]["email"][0],
            "This field may not be blank.",
        )
        self.assertEqual(json_response["message"], "Error. Please try again later.")
