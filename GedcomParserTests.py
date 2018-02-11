import unittest

from GedcomParser import parse_gedcom_file, validate_tag_line, print_individuals_data, print_family_data


class GedcomParseTest(unittest.TestCase):
    """
    Gedcom Data Parsing and Printing Tests.
    """

    def test_parser(self):
        proj2_test_data = parse_gedcom_file("./sampledata/proj02test.ged")
        self.assertTrue(proj2_test_data != [])
        print_individuals_data(proj2_test_data[1])
        print_family_data(proj2_test_data[0], proj2_test_data[1])

    def test_larger_dataset_parser(self):
        other_test_data = parse_gedcom_file("./sampledata/ccorradop02test.ged")
        self.assertTrue(other_test_data != [])
        print_individuals_data(other_test_data[1])
        print_family_data(other_test_data[0], other_test_data[1])

    def test_valid_tag(self):
        self.assertEqual(('0', 'FAM', 'Y', 'f2'), validate_tag_line("0 f2 FAM"))  # Assert 0 f2 FAM is valid

    def test_valid_tag2(self):
        self.assertEqual(('1', 'SEX', 'Y', 'M'), validate_tag_line("1 SEX M"))  # Assert 1 SEX M is valid

    def test_valid_tag3(self):
        self.assertEqual(('1', 'DIV', 'Y', ''), validate_tag_line("1 DIV"))  # Assert 1 DIV is valid

    def test_valid_tag4(self):
        self.assertEqual(('0', 'DIV', 'N', 'invalid'),
                         validate_tag_line("0 DIV invalid"))  # Assert 0 DIV invalid is invalid

    def test_valid_tag5(self):
        self.assertEqual(('1', 'NOTE', 'N', 'bad note'),
                         validate_tag_line("1 NOTE bad note"))  # Assert 1 NOTE bad note is invalid

    def test_valid_tag6(self):
        self.assertEqual(('2', 'BIRT', 'N', 'invalid'),
                         validate_tag_line("2 BIRT invalid"))  # Assert 2 BIRT invalid is invalid

    def test_valid_tag7(self):
        self.assertEqual(('1', 'INVALID', 'N', 'invalid'),
                         validate_tag_line("1 INVALID invalid"))  # Assert 1 INVALID invalid is invalid

    def test_valid_tag8(self):
        self.assertEqual(('0', 'INDI', 'N', 'id'),
                         validate_tag_line("0 INDI id"))  # Assert 0 INDI id is invalid

    def test_valid_tag9(self):
        self.assertEqual(('0', 'FAM', 'N', 'id'),
                         validate_tag_line("0 FAM id"))  # Assert 0 FAM id is invalid

    def test_valid_tag10(self):
        self.assertEqual(('0', 'FAMC', 'N', 'invalid'),
                         validate_tag_line("0 FAMC invalid"))  # Assert 0 FAMC invalid is invalid

    def test_valid_tag11(self):
        self.assertEqual(('0', 'WIFE', 'N', ''),
                         validate_tag_line("0 WIFE"))  # Assert 0 WIFE is invalid


if __name__ == "__main__":
    unittest.main()
