from ....models import WaitlistEntry
from ..base import BaseModelTestCase
from django.db.utils import IntegrityError

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

    def test_create_waitlist_entry(self) -> None:
        # ensure the waitlist entry is created correctly
        self.assertEqual(self.waitlist_entry.email, self.email)

    def test_duplicate_email(self) -> None:
        # check that duplicate email entries are not allowed
        with self.assertRaises(IntegrityError):
            WaitlistEntry.objects.create(email=self.email)

    def test_ordering_by_email(self) -> None:
        # check that entries are ordered by email
        entry1 = WaitlistEntry.objects.create(email="a@example.com")
        entry2 = WaitlistEntry.objects.create(email="z@example.com")
        entries = WaitlistEntry.objects.all()
        self.assertEqual(entries[0], entry1)
        self.assertEqual(entries[1], self.waitlist_entry)
        self.assertEqual(entries[2], entry2)

    def test_verbose_name(self) -> None:
        # check the verbose name
        self.assertEqual(str(WaitlistEntry._meta.verbose_name), "Waitlist Entry")

    def test_verbose_name_plural(self) -> None:
        # check the verbose name plural
        self.assertEqual(
            str(WaitlistEntry._meta.verbose_name_plural), "Waitlist Entries"
        )
