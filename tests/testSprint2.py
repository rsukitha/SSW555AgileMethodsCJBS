import unittest

from GedcomParser import parse_gedcom_file, print_individuals_data, print_family_data, validate_families, \
    validate_individuals


class Sprint1OutputTests(unittest.TestCase):
    """
    Gedcom Data Parsing and Printing Tests For Sprint 2.
    """

    def test_parser(self):
        print("~~~~~~~~~~~~~~~~SPRINT 2 TEST BEGIN~~~~~~~~~~~~~~~~")
        sprint2_data = parse_gedcom_file("./sampledata/sprint2testdata.ged")
        self.assertTrue(sprint2_data != [])
        print_individuals_data(sprint2_data[1], False)
        print_family_data(sprint2_data[0], sprint2_data[1], False)

        validate_families(sprint2_data[0], sprint2_data[1])
        validate_individuals(sprint2_data[1])
        if len(sprint2_data) <= 3:
            for error in sprint2_data[2]:
                print(error + "\n")
        if len(sprint2_data) <= 4:
            for error in sprint2_data[2]:
                print(error + "\n")
            for error in sprint2_data[3]:
                print(error + "\n")
        print("~~~~~~~~~~~~~~~~SPRINT 2 TEST END~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
    unittest.main()
