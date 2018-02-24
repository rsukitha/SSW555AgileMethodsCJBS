import unittest

from GedcomParser import parse_gedcom_file
from models.Individual import Individual


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
        for family in gedcom_data[0]:
            wife = gedcom_data[1].get(gedcom_data[0].get(family).wife_id)
            self.assertTrue(wife.validate_role("WIFE"))
            husb = gedcom_data[1].get(gedcom_data[0].get(family).husband_id)
            self.assertTrue(husb.validate_role("HUSB"))

    def test_correct_gender(self):
        """
        Verify Happy Path
        """
        wife = Individual("wife_one")
        husband = Individual("husb_one")
        husband.gender = "M"
        wife.gender = "F"
        self.assertTrue(wife.validate_role("WIFE"))
        self.assertTrue(husband.validate_role("HUSB"))

    def test_incorrect_gender(self):
        """
        Verify Husband should be male.
        """
        wife = Individual("wife_one")
        husband = Individual("husb_one")
        husband.gender = "F"
        wife.gender = "F"
        self.assertTrue(wife.validate_role("WIFE"))
        self.assertFalse(husband.validate_role("HUSB"))

    def test_incorrect_gender2(self):
        """
        Verify Wife should be female and Husband should be Male
        """
        wife = Individual("wife_one")
        husband = Individual("husb_one")
        husband.gender = "F"
        wife.gender = "M"
        self.assertFalse(wife.validate_role("WIFE"))
        self.assertFalse(husband.validate_role("HUSB"))

    def test_incorrect_gender3(self):
        """
        Verify Wife should be female
        """
        wife = Individual("wife_one")
        husband = Individual("husb_one")
        husband.gender = "M"
        wife.gender = "M"
        self.assertFalse(wife.validate_role("WIFE"))
        self.assertTrue(husband.validate_role("HUSB"))


if __name__ == "__main__":
    unittest.main()
