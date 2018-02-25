"""
Top Level class to execute GEDCOM parsing and manipulation for later storage.
"""

import calendar
import datetime

import prettytable


from models.Family import Family
from models.Individual import Individual

month = {name: num for num, name in enumerate(calendar.month_abbr) if num}


        
def parse_gedcom_file(ccorradop02test):
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
            return parse_valid_results(valid_results)


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


def parse_valid_results(results):
    """
    Method to parse valid results from the GEDCOM file and return INDI/FAM dicts indexed by ID

    :param results -- List of valid GEDCOM results data formatted 'level, tag, valid, args'
    """
    families = {}
    individuals = {}
    current_fam_id = ""
    current_indi_id = ""
    duplicate_fam=[]
    duplicate_ind=[]
    results_iter = iter(results)
    for result in results_iter:
        if result[1] == 'FAM':
            if result[3] in families.keys():                            
                dup_fam_str ='ERROR: FAMILY: US22: Family ID {} is a duplicate.'.format(result[3])
                duplicate_fam.append(dup_fam_str)
            else:
                families[result[3]] = Family(result[3])
                current_fam_id = result[3]
        elif result[1] == 'INDI':
            if result[3] in individuals.keys():     
               dup_ind_str= 'ERROR: INDIVIDUAL: US22: Individual ID {} is a duplicate.' .format(result[3])
               duplicate_ind.append(dup_ind_str)
            else:
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
            indi.validate_birthday()
            indi.set_age()
        elif result[1] == 'DEAT':
            indi = individuals.get(current_indi_id)
            date = next(results_iter)
            indi.death = date[3]
            indi.alive = False
            indi.set_age()
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
    return families, individuals, duplicate_fam, duplicate_ind 


def print_individuals_data(individual_dict, run_validations):
    """
    Method to print and build a table of the Individuals from a GEDCOM file.
    :param individual_dict -- Dictionary containing all Individuals. Key == ID of Individual
    :param run_validations -- boolean whether or not validations should run
    """
    table = prettytable.PrettyTable()
    table.field_names = ('ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse')
    for indi_id, individual in sorted(individual_dict.items()):
        table.add_row(
            [individual.id, individual.name, individual.gender, individual.birthday, individual.age, individual.alive,
             individual.death, individual.child, individual.spouse])
    print("Individuals")
    print(table.get_string())
    if run_validations:
        validate_individuals(individual_dict)


def print_family_data(family_dict, individual_data, run_validations):
    """
    Method to print and build a table of the Families from a GEDCOM file.
    :param family_dict -- Dictionary containing all families. Key == ID of family
    :param individual_data -- Dictionary containing all Individuals. Key == ID of Individual
    :param run_validations -- boolean whether or not validations should run
    """
    table = prettytable.PrettyTable()
    table.field_names = ('ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children')
    for fam_id, family in sorted(family_dict.items()):
        wife_name = ""
        husband_name = ""
        try:
            wife = individual_data[family.wife_id]
            wife_name = wife.name
        except KeyError:
            print("No Wife with ID: ", family.wife_id)

        try:
            husband = individual_data[family.husband_id]
            husband_name = husband.name
        except KeyError:
            print("No Husband with ID: ", family.husband_id)

        table.add_row([family.id, family.married, family.divorced, family.husband_id, husband_name, family.wife_id,
                       wife_name, family.children])
    print("Families")
    print(table.get_string())
    if run_validations:
        validate_families(family_dict, individual_data)


def validate_individuals(individual_dict):
    """
    Method to validate Individuals and print any errors.
    :param individual_dict -- Dictionary containing all Individuals. Key == ID of Individual
    """
    find_upcoming_birthdays(individual_dict)
    for indi_id, individual in sorted(individual_dict.items()):
        individual.verify_date_not_future(individual.id, individual.birthday, "INDIVIDUAL BIRTHDAY")
        individual.verify_date_not_future(individual.id, individual.death, "INDIVIDUAL DEATH")
        individual.validate_birthday()


def validate_families(family_dict, individual_data):
    """
    Method to validate Families and print any errors.
    :param family_dict -- Dictionary containing all families. Key == ID of family
    :param individual_data -- Dictionary containing all Individuals. Key == ID of Individual
    """
    for fam_id, family in sorted(family_dict.items()):
        family.validate_children(individual_data)
        family.birth_before_marriage(individual_data)
        family.verify_date_not_future(fam_id, family.married, "FAMILY MARRIAGE")
        family.verify_date_not_future(fam_id, family.divorced, "FAMILY DIVORCE")
        family.validate_wife_role(individual_data)
        family.validate_husb_role(individual_data)
        family.wife_is_over_14(individual_data)
        family.husband_is_over_14(individual_data)


def unique_name_b_date(ind_dict):
    """
    Determines if individuals have unique names and birth dates
    :param: ind_dict -- Individual dictionary containing all unique individuals
    :return: True if individuals names and birth dates are unique or False otherwise and return error string.
    """
    indi_name_bday_dict = {}
    duplicates = []
    for indi_id in ind_dict:
        if indi_id in ind_dict:
            indi = ind_dict[indi_id]
            if indi.name in indi_name_bday_dict and indi_name_bday_dict[indi.name] == indi.birthday:
                duplicates.append(indi)
                print("ERROR: INDIVIDUAL: US23: {}: Individual with name: {} and birthday {} already exists".format(
                    indi.id, indi.name, indi.birthday))
            indi_name_bday_dict[indi.name] = indi.birthday
    # return whether or not any duplicates existed in the data set.
    return duplicates == []


def find_upcoming_birthdays(individual_dict, today=datetime.datetime.now()):
    """
    Find any upcoming birthdays for all individuals
    :param individual_dict: Dictionary of all Individuals
    :param today: The date time to search birthdays for (today is default)
    """
    birthdays = []
    for individual_id, individual in sorted(individual_dict.items()):
        if individual.upcoming_birthday(today=today):
            birthdays.append(individual.upcoming_birthday(today=today))
    for individual in birthdays:
        print("NOTICE: INDIVIDUAL: US38: {}: Upcoming Birthday on {}".format(individual.id, individual.birthday))

    return birthdays != []
