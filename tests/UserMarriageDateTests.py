import unittest

from GedcomParser import parse_gedcom_file


class UserMarriageDateTests(unittest.TestCase):
    """
    Test Cases for U.S. 10
    """

    def test_husband_is_14(self):
        """
        Validate that the husband is at least 14
        """
        gedcom_data = parse_gedcom_file("../sampledata/us10testdata.ged")
        families = gedcom_data[0]
        for fam_id in gedcom_data[0]:
            family = families[fam_id]
            self.assertFalse(family.husband_is_over_14(gedcom_data[1]))

    def test_wife_is_14(self):
        """
        Validate that the wife is at least 14
        """
        gedcom_data = parse_gedcom_file("../sampledata/us10testdata.ged")
        families = gedcom_data[0]
        for fam_id in gedcom_data[0]:
            family = families[fam_id]
            self.assertTrue(family.wife_is_over_14(gedcom_data[1]))


if __name__ == "__main__":
    unittest.main()
