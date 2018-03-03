import unittest

from GedcomParser import parse_gedcom_file


class IsDeadTests(unittest.TestCase):
    """
    Test Cases for U.S. 03
    """

    def test_us_03_birth_first(self):
        """
        Validate individuals with birthday before death not identified. (False Positive)
        """
        gedcom_data = parse_gedcom_file("./sampledata/US03PosTst.ged")

        individuals = gedcom_data[1]

        for indi_id in individuals:
            individual = individuals[indi_id]
            self.assertTrue(individual.birth_before_death())


    def test_us_03_birth_second(self):
        """
        Validate individuals with birthday after death date are identified. (False Negative)
        """
        gedcom_data = parse_gedcom_file("./sampledata/US03NegTst.ged")

        individuals = gedcom_data[1]

        for indi_id in individuals:
            individual = individuals[indi_id]
            self.assertFalse(individual.birth_before_death())

if __name__ == "__main__":
    unittest.main()
