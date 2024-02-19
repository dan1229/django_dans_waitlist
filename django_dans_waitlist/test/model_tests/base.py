from django.contrib.auth import get_user_model
from django.test import TestCase

"""
# ========================================================================= #
# BASE MODEL TEST CASE ==================================================== #
# ========================================================================= #
"""


class BaseModelTestCase(TestCase):
    base_username = "test_user"
    base_email = "test@email.com"
    base_password = "12345"

    def setUp(self) -> None:
        super(TestCase, self).setUp()

        # USER 1 ====================================== #
        self.base_user = get_user_model().objects.create_user(
            username=self.base_username,
            email=self.base_email,
            password=self.base_password,
        )
        self.client.force_login(self.base_user)
