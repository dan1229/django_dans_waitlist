from api.serializers.base import BaseSerializer
from waitlist.models import WaitlistEntry


#
# WAITLIST ENTRY ================================ #
#
class WaitlistEntrySerializer(BaseSerializer):
    class Meta:
        model = WaitlistEntry
        fields = (
            "id",
            "email",
            "datetime_created",
        )
        read_only_fields = (
            "id",
            "datetime_created",
        )
