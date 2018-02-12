import unittest

from GedcomParser import parse_gedcom_file, validate_tag_line


class GedcomParseTest(unittest.TestCase):
    """
    Gedcom Data Parsing Tests.
    """

    def test_parser(self):
        parse_gedcom_file("./sampledata/proj02test.ged")
        parse_gedcom_file("./sampledata/ccorradop02test.ged")

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


class ValidateBirthdayTest(unittest.TestCase):
    def test_valid_birthday_True(self):
        """
        Testing birthday is less than 150 years.

        """
        date = "04 JAN 2011"
        self.assertTrue(individual.verify_birthday(date))

    def test_invalid_birthday_greater(self):
        """
        Testing birthday is greater than 150 years.

        """
        date = "04 JAN 2099"
        self.assertFalse(individual.verify_birthday(date))


    def test_valid_birthday_equal(self):

        """
        Testing birthday is equal to 150 years.

        """
        date = "04 JAN 2015"
        self.assertEqual(individual.verify_birthday(date))


    def test_valid_birthday_notEqual(self):
        """
        Testing birthday is equal to 150 years.

        """
        date = "04 JAN 2009"
        self.assertNotEqual(individual.verify_birthday(date))


    def test_valid_birthday_IsnotNone(self):
        """
        Testing birthday is not none.

        """
        date = "04 JAN 2011"
        self.assertIsNotNone(individual.verify_birthday(date))



if __name__ == "__main__":
    unittest.main()
