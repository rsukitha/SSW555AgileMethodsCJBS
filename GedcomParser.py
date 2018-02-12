"""
Top Level class to execute GEDCOM parsing and manipulation for later storage.
"""
import prettytable

from models.Family import Family
from models.Individual import Individual
import datetime


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
            print_family_data(data[0], data[1])


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
            validate_dates(date, indi)
            indi.birthday = date[3]
            indi.set_age()
        elif result[1] == 'DEAT':
            indi = individuals.get(current_indi_id)
            date = next(results_iter)
            validate_dates(date, indi)
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
            validate_dates(date, current_fam_id)
            validate_marriage_date(indi.birthday, date, indi)
            fam.married = date[3]
        elif result[1] == 'DIV':
            fam = families.get(current_fam_id)
            date = next(results_iter)
            validate_dates(date, fam)
            fam.divorced = date[3]
    return families, individuals

def get_date(date):
      """
      Method to get the date from input and convert it to Date format
      :param date -- Input line tuple in format (level, tag, valid, arg)      
      """      
      month = {"JAN": 1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7, "AUG":8, "SEP":9, "OCT":10, "NOV":11, "DEC":12}
      split_date = date[3].split(" ")
      given_year = int(split_date[2])
      given_month = month[split_date[1]]
      given_day = int(split_date[0])
      given_date = datetime.date(given_year, given_month, given_day)
      
      return given_date
      
      
def validate_dates(date, current_indi_id):
      """
      Method to validate if the birth, death, marriage, divorce dates are before today
      :param date -- Input line tuple in format (level, tag, valid, arg) 
      :param current_indi_id -- Individual object
      """   
      current_date = datetime.datetime.now()
      year = current_date.year
      month = current_date.month
      day = current_date.day
      today = datetime.date(year, month, day)
      

      given_date = get_date(date)

      if given_date > today:
            print("Invalid! Birth, Marriage, Divorce or Death dates should not be after today. User ID is: ", current_indi_id.id, " and today is: ", today)            
      else:
            pass

def validate_marriage_date(birth, marriage, current_fam_id):
      """
      Method to validate if the person is born before his/her marriage
      :param birth -- Birthdate of the person
      :param marriage -- Input line tuple in format (level, tag, valid, arg) 
      :param current_fam_id -- Family object
      """   
      month = {"JAN": 1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7, "AUG":8, "SEP":9, "OCT":10, "NOV":11, "DEC":12}
      
      birth = birth.split(" ")
      birth_year = int(birth[2])
      birth_month = month[birth[1]]
      birth_day = int(birth[0])
      birth_date = datetime.date(birth_year, birth_month, birth_day)
      
      marriage_date = get_date(marriage)

      if marriage_date < birth_date:
            print("Invalid! Birth should occur before marriage for user: ", current_fam_id.id)
      else:
            pass  

def print_individuals_data(individual_dict):
    """
    Method to print and build a table of the Individuals from a GEDCOM file.
    :param individual_dict -- Dictionary containing all Individuals. Key == ID of Individual
    """
    table = prettytable.PrettyTable()
    table.field_names = ('ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse')
    for indi_id, individual in sorted(individual_dict.items()):
        table.add_row(
            [individual.id, individual.name, individual.gender, individual.birthday, individual.age, individual.alive,
             individual.death, individual.child, individual.spouse])
    print("Individuals")
    print(table.get_string())


def print_family_data(family_dict, individual_data):
    """
    Method to print and build a table of the Families from a GEDCOM file.
    :param family_dict -- Dictionary containing all families. Key == ID of family
    :param individual_data -- Dictionary containing all Individuals. Key == ID of Individual
    """
    table = prettytable.PrettyTable()
    table.field_names = ('ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children')
    for fam_id, family in sorted(family_dict.items()):
        wife_name = ""
        husband_name = ""
        try:
            wife_name = individual_data[family.wife_id].name
        except KeyError:
            print("No Wife with ID: ", family.wife_id)

        try:
            husband_name = individual_data[family.husband_id].name
        except KeyError:
            print("No Husband with ID: ", family.husband_id)

        table.add_row([family.id, family.married, family.divorced, family.husband_id, husband_name, family.wife_id,
                       wife_name, family.children])
    print("Families")
    print(table.get_string())
