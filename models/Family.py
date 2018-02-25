"""
Class to represent a Family based on GEDCOM data sets.
"""
import datetime

from models.Member import Member


class Family(Member):
    __slots__ = "id", "married", "divorced", "husband_id", "husband_name", "wife_id", "wife_name", "children"

    def __init__(self, unique_id):
        self.id = unique_id
        self.children = {}
        self.wife_id = ""
        self.husband_id = ""
        self.husband_name = "NA"
        self.wife_name = "NA"
        self.divorced = "NA"
        self.married = "NA"

    def validate_children(self, individuals):
        """
        U.S. 25 Validates whether a Child with the same name and birthday exists in the family.
        """
        child_name_bday_dict = {}
        duplicates = []
        for child_id in self.children:
            if child_id in individuals:
                child = individuals[child_id]
                if child.name in child_name_bday_dict and child_name_bday_dict[child.name] == child.birthday:
                    duplicates.append(child)
                    print("ERROR: FAMILY: US25: {}: Child with name: {} and birthday {} already exists".format(
                        self.id, child.name, child.birthday))
                child_name_bday_dict[child.name] = child.birthday
        return duplicates == []

    def marriage_before_14(self, individuals):
        """
        verify if marriage age is valid
        """
        for indi_id in individuals:
            individual = individuals[indi_id]
            if individual.id == self.wife_id or individual.id == self.husband_id:
                if individual.calculate_age() < 14:
                    print("ERROR: INDIVIDUAL: US10: {}: Individual Married on {} before birth on {}".format(
                        self.id,
                        self.married,
                        individual.birthday))
                return individual.calculate_age() >= 14

    def birth_before_marriage(self, individuals):
        """
        Verify if marriage is after birth.
        """
        bad_dates = []
        formatted_marriage = datetime.datetime.strptime(self.married, '%d %b %Y')
        for indi_id in individuals:
            individual = individuals[indi_id]
            if individual.id == self.husband_id or individual.id == self.wife_id:
                formatted_birthday = datetime.datetime.strptime(individual.birthday, '%d %b %Y')
                if formatted_marriage < formatted_birthday:
                    bad_dates.append(formatted_marriage)
                    print(
                        "ERROR: INDIVIDUAL: US02: {}: Individual Born before Marriage on {}".format(self.id,
                                                                                                    formatted_marriage
                                                                                                    .strftime(
                                                                                                        "%m %d %Y")))
        return bad_dates == []

    def validate_wife_role(self, individuals):
        """
        Method to validate gender to wife role for an individual.

        :param individuals: individual data
        :return: True if gender is valid for role.
        """
        if self.wife_id in individuals:
            wife = individuals[self.wife_id]
            if wife.gender == "M":
                print(
                    "ERROR: INDIVIDUAL: US21: {}: Spouse with gender: {} and role {} do not match".format(wife.id,
                                                                                                          wife.gender,
                                                                                                          "WIFE"))
                return False
            return True

    def validate_husb_role(self, individuals):
        """
        Method to validate gender to wife role for an individual.

        :param individuals: individual data
        :return: True if gender is valid for role.
        """
        if self.husband_id in individuals:
            husband = individuals[self.husband_id]
            if husband.gender == "F":
                print(
                    "ERROR: INDIVIDUAL: US21: {}: Spouse with gender: {} and role {} do not match".format(husband.id,
                                                                                                          husband.gender,
                                                                                                          "HUSB"))
                return False
            return True
