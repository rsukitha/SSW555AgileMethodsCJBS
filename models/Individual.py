"""
Class to represent an Individual based on GEDCOM Data
"""
import datetime

from models.Family import Family
from models.Member import Member


class Individual(Member):
    __slots__ = "id", "name", "gender", "birthday", "age", "alive", "death", "child", "spouse"

    def __init__(self, unique_id):
        self.id = unique_id
        self.child = {}
        self.spouse = {}
        self.age = ""
        self.birthday = ""
        self.gender = ""
        self.alive = True
        self.death = "NA"

    def validate_birthday(self):
        if not self.verify_date_150_years(self.birthday):
            print(
                "ERROR: INDIVIDUAL: US10: {}: Individual Birthday {} over 150 years ago.".format(self.id,
                                                                                                 self.birthday))

    def set_age(self):
        self.age = self.calculate_age()

    def upcoming_birthday(self, today=datetime.datetime.now()):
        """
        Prints whether this user's birthday is upcoming
        :return: True if birthday is upcoming
        """
        current_year_bday_str = datetime.datetime.strptime(self.birthday, '%d %b %Y').strftime(
            "%m %d") + " " + str(today.year)
        current_year_bday = datetime.datetime.strptime(current_year_bday_str, '%m %d %Y')
        delta_from_birthday = current_year_bday - today
        if 0 <= delta_from_birthday.days <= 30:
            return self
        else:
            return False

    def calculate_age(self):
        """
        Calculate Age Based on Birthday
        :return: Integer representation of Age
        """
        birthday = datetime.datetime.strptime(self.birthday, '%d %b %Y')
        today = datetime.datetime.now()
        if self.death != "NA":
            death_date = datetime.datetime.strptime(self.death, '%d %b %Y')
            if death_date <= today:
                return int(abs(death_date.year)) - int(abs(birthday.year))
        return int(abs(today.year)) - int(abs(birthday.year))

    def validate_role(self, role):
        """
        Method to validate gender to role for an individual.

        :param role: "WIFE" or "HUSB"
        :return: True if gender is valid for role.
        """
        if self.gender == "M" and role == "HUSB":
            return True
        if self.gender == "F" and role == "WIFE":
            return True
        print(
            "ERROR: INDIVIDUAL: US21: {}: Spouse with gender: {} and role {} do not match".format(self.id, self.gender,
                                                                                                  role))
        return False

    def validate_marriage(self):
        """
        verify if marriage age is valid
        """
        if Individual.id == Family.wife_id or Individual.id == Family.husband_id:
            return self.calculate_age() >= 14
