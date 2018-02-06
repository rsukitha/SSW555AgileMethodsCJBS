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
Modified February 4th, 2018

"""

import os
import unittest

import prettytable as prettytable


class GedcomParseTest(unittest.TestCase):
    """
    Gedcom Data Parsing Tests.
    """

    def test_parser(self):
        parse_gedcom_file("./proj02test.ged")
        parse_gedcom_file("./ccorradop02test.ged")

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


class Individual:
    __slots__ = "id", "name", "gender", "birthday", "age", "alive", "death", "child", "spouse"

    def __init__(self, unique_id):
        self.id = unique_id
        self.child = {}
        self.spouse = {}
        self.age = ""
        self.alive = True
        self.death = ""
        # TODO define age determinations based on birthday.


class Family:
    __slots__ = "id", "married", "divorced", "husband_id", "husband_name", "wife_id", "wife_name", "children"

    def __init__(self, unique_id):
        self.id = unique_id
        self.children = {}
        self.husband_name = ""
        self.wife_name = ""
        self.divorced = ""
        # TODO Define how to reference names based on IDs


def validate_tag_line(gedcom_line):
    """
    Method to validate the given tag and associated level.

    :param gedcom_line: This is a sample line from a gedcom file
    :return: list containing
    """
    # Dictionary of All Valid Tags for each level.
    valid_tags = {'0': ('HEAD', 'NOTE', 'TRLR'),
                  '1': ('BIRT', 'CHIL', 'DEAT', 'DIV', 'FAMC', 'FAMS', 'HUSB', 'MARR', 'NAME', 'SEX', 'WIFE'),
                  '2': ('DATE')}

    gedcom_tokens = gedcom_line.split()

    if len(gedcom_tokens) == 3 and gedcom_tokens[0] == '0' and gedcom_tokens[2] in ('INDI', 'FAM'):
        level, args, tag = gedcom_tokens
        valid = 'Y'
    elif len(gedcom_tokens) >= 2:
        level, tag, args = gedcom_tokens[0], gedcom_tokens[1], " ".join(gedcom_tokens[2:])
        valid = 'Y' if level in valid_tags and tag in valid_tags[level] else 'N'
    else:
        level, tag, valid, args = gedcom_tokens, 'NA', 'N', 'NA'

    return level, tag, valid, args


def parse_gedcom_file(file_path):
    """
    Helper method to parse the file from input.
    """
    try:
        file = open(file_path)
    except FileNotFoundError:
        print("Cannot open file: " + str(file_path))
    except IsADirectoryError:
        print("This is a directory: " + str(file_path))
    else:
        with file:
            valid_results = []
            for line in file.readlines():
                # print('--> ' + line.strip())
                result = validate_tag_line(line)
                if result[2] == 'Y':
                    valid_results.append(result)

                    # print('<-- {}|{}|{}|{}\n'.format(result[0], result[1], result[2], result[3]))
            data = parse_valid_results(valid_results)
            print_individuals_data(data[1])
            print_family_data(data[0])


def print_individuals_data(individual_dict):
    """
    Method to print and build a table of the Individuals from a GEDCOM file.
    """
    table = prettytable.PrettyTable()
    table.field_names = ('ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse')
    for indi_id, individual in sorted(individual_dict.items()):
        table.add_row(
            [individual.id, individual.name, individual.gender, individual.birthday, individual.age, individual.alive,
             individual.death, individual.child, individual.spouse])
    print("Individuals")
    print(table.get_string())


def print_family_data(family_dict):
    """
    Method to print and build a table of the Families from a GEDCOM file.
    """
    table = prettytable.PrettyTable()
    table.field_names = ('ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children')
    for fam_id, family in sorted(family_dict.items()):
        table.add_row(
            [family.id, family.married, family.divorced, family.husband_id, family.husband_name, family.wife_id,
             family.wife_name, family.children])
    print("Families")
    print(table.get_string())


def parse_valid_results(results):
    """
    Method to parse valid results from the GEDCOM file and return INDI/FAM dicts indexed by ID

    :param results -- List of valid GEDCOM results data formatted 'level, tag, valid, args'
    """
    families = {}
    individuals = {}
    current_fam_id = ""
    current_indi_id = ""
    results_iter = iter(results)
    for result in results_iter:
        if result[1] == 'FAM':
            families[result[3]] = Family(result[3])
            current_fam_id = result[3]
        elif result[1] == 'INDI':
            individuals[result[3]] = Individual(result[3])
            current_indi_id = result[3]
        elif result[1] == 'NAME':
            individuals.get(current_indi_id).name = result[3]
        elif result[1] == 'SEX':
            individuals.get(current_indi_id).gender = result[3]
        elif result[1] == 'BIRT':
            indi = individuals.get(current_indi_id)
            date = next(results_iter)
            indi.birthday = date[3]
        elif result[1] == 'DEAT':
            indi = individuals.get(current_indi_id)
            date = next(results_iter)
            indi.death = date[3]
            indi.alive = False
        elif result[1] == 'FAMC':
            individuals.get(current_indi_id).child[result[3]] = result[3]
        elif result[1] == 'FAMS':
            individuals.get(current_indi_id).spouse[result[3]] = result[3]
        elif result[1] == 'HUSB':
            families.get(current_fam_id).husband_id = result[3]
        elif result[1] == 'WIFE':
            families.get(current_fam_id).wife_id = result[3]
        elif result[1] == 'CHIL':
            families.get(current_fam_id).children[result[3]] = result[3]
        elif result[1] == 'MARR':
            fam = families.get(current_fam_id)
            date = next(results_iter)
            fam.married = date[3]
        elif result[1] == 'DIV':
            fam = families.get(current_fam_id)
            date = next(results_iter)
            fam.divorced = date[3]
    return families, individuals


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
