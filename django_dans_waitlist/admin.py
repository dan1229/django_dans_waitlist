from django.contrib import admin
from .models import WaitlistEntry


#
# WAITLIST ENTRY ========================= #
#
class WaitlistEntryAdmin(admin.ModelAdmin):  # type: ignore[type-arg]
    list_display = (
        "email",
        "datetime_created",
    )

    search_fields = (
        "id",
        "email",
        "datetime_created",
    )
    readonly_fields = ("id",)
    list_per_page = 100


#
# REGISTER ========================= #
#
admin.site.register(WaitlistEntry, WaitlistEntryAdmin)
