import unittest

from GedcomParser import parse_gedcom_file


class IsDeadTests(unittest.TestCase):
    """
    Test Cases for U.S. 29
    """

    def test_us_29_not_dead(self):
        """
        Validate individuals living are not identified as dead. (False Positive)
        """
        gedcom_data = parse_gedcom_file("./sampledata/US29NegTst.ged")

        individuals = gedcom_data[1]
        outcome = []
        result = False
        for indi_id in individuals:
            individual = individuals[indi_id]
            result = individual.is_dead()
            if result:
                outcome.append(result)
        self.assertFalse(result)

    def test_us_29_is_dead(self):
        """
        Validate individuals dead are not identified as living. (False Negative)
        """
        gedcom_data = parse_gedcom_file("./sampledata/US29PosTstx2.ged")

        individuals = gedcom_data[1]
        outcome = []
        result = False
        for indi_id in individuals:
            individual = individuals[indi_id]
            result = individual.is_dead()
            if result:
                outcome.append(result)
        self.assertTrue(result)



if __name__ == "__main__":
    unittest.main()