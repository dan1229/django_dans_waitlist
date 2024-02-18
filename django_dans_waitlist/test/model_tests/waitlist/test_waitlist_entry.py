from waitlist.models import WaitlistEntry
from core.test.model_tests.base import BaseModelTestCase

"""
# ========================================================================= #
# TEST WAITLIST ENTRY ===================================================== #
# ========================================================================= #
"""


class TestWaitlistEntry(BaseModelTestCase):
    email = "waitlistemail@example.com"

    def setUp(self) -> None:
        self.waitlist_entry = WaitlistEntry.objects.create(email=self.email)
        super(TestWaitlistEntry, self).setUp()

    # =================================================================== #
    # BASIC TESTS ======================================================= #
    # =================================================================== #

    def test_str(self) -> None:
        # check properties
        self.assertIn(self.email, str(self.waitlist_entry))
        self.assertNotEqual(str(self.waitlist_entry), None)
