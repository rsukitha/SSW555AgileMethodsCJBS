import datetime
import unittest

from GedcomParser import parse_gedcom_file


class UpcomingAnniversariesTests(unittest.TestCase):
    """
    Test Cases for U.S. 39
    """

    def test_us_39(self):
        """
        Validate that there are upcoming anniversaries for 2/21/2017 in this file.
        """
        gedcom_data = parse_gedcom_file("./sampledata/us39testdata.ged")
        families = gedcom_data[0]
        individuals = gedcom_data[1]
        data = []
        # Assert that this file contains upcoming anniversaries for febraury.
        today = datetime.datetime.strptime("02 21 2017", '%m %d %Y')
        for fam_id in families:
            family = families[fam_id]
            result = family.anniversary_upcoming(individuals, today=today)
            if result:
                data.append(result)
        self.assertFalse(data == [])

    def test_us_39_neg(self):
        """
        Validate that there are NO upcoming anniversaries for 12/21/2017 in this file.
        """
        gedcom_data = parse_gedcom_file("./sampledata/us39testdata.ged")
        families = gedcom_data[0]
        individuals = gedcom_data[1]
        data = []
        # Assert that this file contains NO upcoming anniversaries for december.
        today = datetime.datetime.strptime("12 21 2017", '%m %d %Y')
        for fam_id in families:
            family = families[fam_id]
            result = family.anniversary_upcoming(individuals, today=today)
            if result:
                data.append(result)
        self.assertTrue(data == [])


if __name__ == "__main__":
    unittest.main()
