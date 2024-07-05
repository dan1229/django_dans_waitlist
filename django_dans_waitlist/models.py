import uuid
from typing import List
from django.db import models

"""
# ==================================================================================== #
# ABSTRACT BASE MODEL ================================================================ #
# ==================================================================================== #
"""


class AbstractBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # type: ignore[var-annotated]
    datetime_created = models.DateTimeField(auto_now_add=True, editable=False)  # type: ignore[var-annotated]
    datetime_modified = models.DateTimeField(auto_now=True)  # type: ignore[var-annotated]

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
    email = models.EmailField(unique=True)  # type: ignore[var-annotated]

    def __str__(self) -> str:
        return f"Waitlist Entry: {self.email}"

    class Meta:
        ordering: List[str] = ["email"]
        verbose_name: str = "Waitlist Entry"
        verbose_name_plural: str = "Waitlist Entries"
