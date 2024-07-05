import uuid
from typing import Any, List
from django.db import models

"""
# ==================================================================================== #
# ABSTRACT BASE MODEL ================================================================ #
# ==================================================================================== #
"""


class AbstractBaseModel(models.Model):
    id: models.UUIDField[uuid.UUID, Any] = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    datetime_created: models.DateTimeField[Any, Any] = models.DateTimeField(
        auto_now_add=True, editable=False
    )
    datetime_modified: models.DateTimeField[Any, Any] = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True
        ordering: List[str] = ["datetime_created"]

    def __str__(self) -> str:
        return "Abstract Base Model"


"""
# ==================================================================================== #
# WAITLIST ENTRY ===================================================================== #
# ==================================================================================== #
"""


class WaitlistEntry(AbstractBaseModel):
    email: models.EmailField[str, Any] = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f"Waitlist Entry: {self.email}"

    class Meta:
        ordering: List[str] = ["email"]
        verbose_name: str = "Waitlist Entry"
        verbose_name_plural: str = "Waitlist Entries"
