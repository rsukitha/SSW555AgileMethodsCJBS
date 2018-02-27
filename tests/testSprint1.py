import unittest

from GedcomParser import parse_gedcom_file, print_individuals_data, print_family_data, validate_families, \
    validate_individuals


class Sprint1OutputTests(unittest.TestCase):
    """
    Gedcom Data Parsing and Printing Tests For Sprint 1.
    """

    def test_parser(self):
        print("~~~~~~~~~~~~~~~~SPRINT 1 TEST BEGIN~~~~~~~~~~~~~~~~")
        sprint1_data = parse_gedcom_file("./sampledata/sprint1testdata.ged")
        self.assertTrue(sprint1_data != [])
        print_individuals_data(sprint1_data[1], False)
        print_family_data(sprint1_data[0], sprint1_data[1], False)

        validate_families(sprint1_data[0], sprint1_data[1])
        validate_individuals(sprint1_data[1])
        print("~~~~~~~~~~~~~~~~SPRINT 1 TEST END~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    unittest.main()
