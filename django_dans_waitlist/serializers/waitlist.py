from django_dans_api_toolkit.serializers.base import BaseSerializer
from ..models import WaitlistEntry


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
