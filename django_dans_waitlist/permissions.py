from typing import Any
from rest_framework import permissions
from rest_framework.request import Request

"""
============================================================================================ #
BASE PERMISSIONS =========================================================================== #
============================================================================================ #
"""


class AdminOnly(permissions.BasePermission):
    """Allows access only to Admins."""

    def has_permission(self, request: Request, view: Any) -> bool:
        if request.user.is_authenticated and request.user.is_staff:
            return True
        return False
