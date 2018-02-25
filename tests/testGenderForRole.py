import unittest

from GedcomParser import parse_gedcom_file


class GenderForRoleTests(unittest.TestCase):
    """
    Test Cases for U.S. 21
    """

    def test_integration(self):
        """
        This is a sanity check on the integration with some sample data.
        Verify that Cheryl is F and Jimmy is M.
        """
        gedcom_data = parse_gedcom_file("../sampledata/us21testdata.ged")
        families = gedcom_data[0]
        individuals = gedcom_data[1]
        for fam_id in families:
            family = families[fam_id]
            self.assertTrue(family.validate_husb_role(individuals))
            self.assertTrue(family.validate_wife_role(individuals))

    def test_integration_neg(self):
        """
        This is a sanity check on the integration with some sample data.
        Verify that Cheryl is F and Jimmy is M.
        """
        gedcom_data = parse_gedcom_file("../sampledata/us21negtestdata.ged")
        families = gedcom_data[0]
        individuals = gedcom_data[1]
        for fam_id in families:
            family = families[fam_id]
            self.assertFalse(family.validate_husb_role(individuals))
            self.assertFalse(family.validate_wife_role(individuals))


if __name__ == "__main__":
    unittest.main()
