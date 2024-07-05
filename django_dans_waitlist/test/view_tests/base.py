from typing import Any
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory
from django.contrib.auth import get_user_model

"""
# =============================================================================================
# BASE API TEST CASE ==========================================================================
# =============================================================================================
"""


class BaseAPITestCase(APITestCase):
    username = "test"
    email_user = "test@test.com"
    password = "password"

    def setUp(self) -> None:
        super(APITestCase, self).setUp()

        # store standard api factory
        self.factory = APIRequestFactory()

        # create user
        self.user = get_user_model().objects.create(
            username=self.username, email=self.email_user, password=self.password
        )
        self.user_token = Token.objects.create(user=self.user)

    # TOKEN FUNCTIONS

    def get_headers(self, user: Any) -> str:
        return f"Token {self.get_token(user)}"

    def get_token(self, user: Any) -> Token:
        return Token.objects.get_or_create(user=user)[0]
