"""
Project 02
Author: Chris Corrado
SSW 555: Agile Methods in Software Engineering

Deliverables:

your program source code
your test GEDCOM file
the output of running your program on your test GEDCOM file
the output of running your program against the input test file on Canvas

Created January 30th, 2018

"""

import os
import unittest


class GedcomParseTest(unittest.TestCase):
    """
    Gedcom Data Parsing Tests.
    """

    def test_parser(self):
        parse_gedcom_file("./proj02test.ged")
        # parse_gedcom_file("./ccorradop02test.ged")

    def test_valid_tag(self):
        self.assertTrue(
            validate_tag_line("0", "NOTE", "NOTE"))  # Assert that NOTE can have NOTE as val 0 (top == selct)

    def test_valid_tag2(self):
        self.assertFalse(validate_tag_line("0", "FAM", "BIRT"))  # Assert BIRT cannot have a FAM as val 0.

    def test_valid_tag3(self):
        self.assertFalse(validate_tag_line("3", "NOTE", ""))  # Assert 3 is invalid value.

    def test_valid_tag4(self):
        self.assertTrue(validate_tag_line("2", "DATE", "BIRT"))  # Assert BIRT can have a DATE as val 2

    def test_valid_tag5(self):
        self.assertTrue(validate_tag_line("1", "HUSB", "FAM"))  # Assert a FAM can have a HUSB as val 1

    def test_valid_tag6(self):
        self.assertFalse(validate_tag_line("1", "NOTE", "INDI"))  # Assert that INDI cannot have NOTE as val 1

    def test_valid_tag7(self):
        self.assertTrue(validate_tag_line("1", "FAMC", "INDI"))  # Assert that an INDI can have a FAMC as val 1


def validate_tag_line(selected_level, selected_tag, current_top_tag):
    """
    Method to validate the given tag and associated level.

    :param selected_level: level 0, 1, or 2.
    :param selected_tag:     e.g."NAME", "SEX", "BIRT", etc
    :param current_top_tag: e.g. "INDI", "FAM", "HEAD", "TRLR", etc
    :return: true if valid.
    """
    # Tuple of valid levels
    valid_levels = ('0', '1', '2')

    # Gut check on valid levels.
    if selected_level not in valid_levels:
        return False

    # Dont support Dates not level 2
    if selected_tag == "DATE" and selected_level != '2':
        return False

    # Tuple of all valid Level 0 tags
    level_0_tags = ("INDI", "FAM", "HEAD", "TRLR", "NOTE")

    # Tuple of valid INDI tags
    valid_indi_tags = ("NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS")

    # Tuple of valid FAM tags
    valid_fam_tags = ("MARR", "HUSB", "WIFE", "CHIL", "DIV")

    # Tuple of valid DATE tags
    valid_date_tags = ("BIRT", "DEAT", "DIV", "MARR")

    level_dict = dict()
    level_dict["0"] = level_0_tags
    level_dict["1"] = valid_fam_tags + valid_indi_tags
    level_dict["2"] = "DATE"

    # If the user passes in a top tag as the current tag and the level is 0, immediately validate
    if selected_tag in level_0_tags and selected_tag is current_top_tag and selected_level == '0':
        return True

    # Validate if the selected tag is even a valid tag.
    if selected_tag not in (valid_indi_tags + valid_fam_tags + valid_date_tags + ("DATE", "DATE")):
        return False

    # if for the current selected tag the level is not valid, return False.
    if selected_tag not in level_dict[selected_level]:
        return False

    tag_dict = dict()
    tag_dict["INDI"] = valid_indi_tags
    tag_dict["FAM"] = valid_fam_tags
    tag_dict["DATE"] = valid_date_tags
    tag_dict["HEAD"] = ""
    tag_dict["TRLR"] = ""
    tag_dict["NOTE"] = ""

    # Validate if the selected tag is in the valid set of tags for the current top tag.
    if selected_level == '0' and selected_tag not in tag_dict[level_0_tags]:
        return False

    # All Validations Passed
    return True


def parse_gedcom_file(file_path):
    """
    Helper method to parse the file from input.
    """

    # Tuple of supported tags
    valid_tags = ("NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "DATE",
                  "MARR", "HUSB", "WIFE", "CHIL", "DIV", "INDI", "FAM", "HEAD", "TRLR", "NOTE")

    try:
        file = open(file_path)
    except FileNotFoundError:
        print("Cannot open file: " + str(file_path))
    except IsADirectoryError:
        print("This is a directory: " + str(file_path))
    else:
        with file:
            top_tag = ""
            for line in file.readlines():
                print('--> ' + line.strip())
                current_line = line.strip().split(" ")
                current_level = current_line[0]
                current_tag = current_line[1]
                is_valid = "N"
                current_arguments = " ".join(current_line[2:])
                # Support cases where the current tag could be in the 3rd position of the line.
                if current_tag not in valid_tags:
                    if len(current_line) >= 3:
                        current_tag = current_line[2]
                        current_arguments = current_line[1]
                if current_level == '0':
                    top_tag = current_tag
                if validate_tag_line(current_level, current_tag, top_tag):
                    is_valid = "Y"
                print('<-- {}|{}|{}|{}\n'.format(current_level, current_tag, is_valid, current_arguments))


def validate_gedcom_file(directory):
    """
    Method to validate the Gedcom File based on a dir containing the file
    :param directory: The directory to get the file from.
    """
    os.chdir(directory)
    for file in os.listdir(directory):
        if str(file).endswith(".ged"):
            parse_gedcom_file(file)
            break
    else:
        print("No .ged files found!")


if __name__ == "__main__":
    unittest.main()
