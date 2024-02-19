#  Created by Daniel Nazarian on 8/8/21, 1:13 PM
#  Copyright (c) Daniel Nazarian. 2021 . All rights reserved.
#
#  Please do NOT use, edit, distribute, or otherwise use this code without consent.
#  For questions, comments, concerns, and more -> dnaz@danielnazarian.com
from rest_framework.routers import DefaultRouter
from .views import (
    WaitlistEntryEmailViewSet,
    WaitlistEntryViewSet,
)


"""
# =================================================================================================== #
# URLS ============================================================================================== #
# =================================================================================================== #
"""

# Create a router and register our view sets with it
router = DefaultRouter()
router.register(r"entries", WaitlistEntryViewSet)
router.register(r"entries/emails", WaitlistEntryEmailViewSet)
urlpatterns = router.urls
