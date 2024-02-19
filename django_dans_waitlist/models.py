from django.db import models
from core.models import AbstractBaseModel


#
# WAITLIST ENTRY ========================= #
#
class WaitlistEntry(AbstractBaseModel):
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f"Waitlist Entry: {self.email}"

    class Meta:
        app_label = "waitlist"
        ordering = ["email"]
        verbose_name = "Waitlist Entry"
        verbose_name_plural = "Waitlist Entries"
