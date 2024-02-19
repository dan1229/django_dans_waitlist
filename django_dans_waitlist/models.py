import uuid

from django.db import models

"""
# ==================================================================================== #
# ABSTRACT BASE MODEL ================================================================ #
# ==================================================================================== #
"""


class AbstractBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    datetime_created = models.DateTimeField(auto_now_add=True, editable=False)
    datetime_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["datetime_created"]

    def __str__(self):
        return "Abstract Base Model"


"""
# ==================================================================================== #
# WAITLIST ENTRY ===================================================================== #
# ==================================================================================== #
"""


class WaitlistEntry(AbstractBaseModel):
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f"Waitlist Entry: {self.email}"

    class Meta:
        app_label = "waitlist"
        ordering = ["email"]
        verbose_name = "Waitlist Entry"
        verbose_name_plural = "Waitlist Entries"
