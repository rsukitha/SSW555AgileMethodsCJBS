import unittest

from GedcomParser import parse_gedcom_file


class UserMarriageDateTests(unittest.TestCase):
    """
    Test Cases for U.S. 30 and US 31
    """

    def test_living_marrried(self):
        """
        Lists all living married people
        """
        gedcom_data = parse_gedcom_file("./sampledata/us30testdata.ged")
        famil = gedcom_data[0]
        individ=gedcom_data[1]
        for fam_id in gedcom_data[0]:
            family = famil[fam_id]
        self.assertTrue(family.validate_living_married(individ,famil))


    def test_living_single_over_30(self):
        """
        Lists all living single people over 30
        """
        gedcom_data = parse_gedcom_file("./sampledata/us30testdata.ged")
        famil = gedcom_data[0]
        individ=gedcom_data[1]
        for individual_id in gedcom_data[1]:
            individual = individ[individual_id]
        self.assertTrue(individual.validate_living_single_over_30(individ,famil))



if __name__ == "__main__":
    unittest.main()
