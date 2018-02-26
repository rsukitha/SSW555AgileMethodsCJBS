import datetime
import unittest

from GedcomParser import parse_gedcom_file, find_upcoming_birthdays


class UpcomingBirthdayTests(unittest.TestCase):
    """
    Test Cases for U.S. 38
    """

    def test_us_38(self):
        """
        Validate that there are upcoming birthdays for 2/21/2017 in this file.
        """
        gedcom_data = parse_gedcom_file("./sampledata/us25testdata.ged")
        individuals = gedcom_data[1]
        # Assert that this file contains upcoming birthdays for febraury.
        today = datetime.datetime.strptime("02 21 2017", '%m %d %Y')
        self.assertTrue(find_upcoming_birthdays(individuals, today=today))

    def test_us_38_neg(self):
        """
        Validate that there are NO upcoming birthdays for 12/21/2017 in this file.
        """
        gedcom_data = parse_gedcom_file("./sampledata/us25testdata.ged")
        individuals = gedcom_data[1]
        # Assert that this file contains NO upcoming birthdays for december.
        today = datetime.datetime.strptime("12 21 2017", '%m %d %Y')
        self.assertFalse(find_upcoming_birthdays(individuals, today=today))


if __name__ == "__main__":
    unittest.main()
