"""
Class to represent an Individual based on GEDCOM Data
"""
import datetime

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
                "ERROR: INDIVIDUAL: US07: {}: Individual Birthday {} over 150 years ago.".format(self.id,
                                                                                                 self.birthday))

    def validate_death(self):
        if not self.verify_date_150_years(self.birthday):
            print(
                "ERROR: INDIVIDUAL: US07: {}: Individual Death {} over 150 years ago.".format(self.id,
                                                                                              self.birthday))

    def set_age(self):
        self.age = self.calculate_age()

    def upcoming_birthday(self, today=datetime.datetime.now()):
        """
        Prints whether this user's birthday is upcoming
        :return: True if birthday is upcoming
        """
        if self.return_upcoming_date(self.birthday, today):
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

    def validate_spouse(self, child_id):

        if child_id in self.child:
            print("ERROR: INDIVIDUAL: US17: {}: Marriage cannot happen with descendants: {}.".format(self.id,
                                                                                                     child_id))
            return False
        return True

    def is_dead(self):
        """
        US 29: List all deceased individuals in a GEDCOM file
        :return: True if if dead
        """
        if self.death != "NA":
            print("NOTICE: INDIVIDUAL: US29: {}: Individual Named {} is deceased".format(self.id, self.name))
            return True
        return False

    @staticmethod
    def validate_living_single_over_30(individuals, families):
        alive_single = set()
        for indiv in sorted(individuals.items()):
            for fam in sorted(families.items()):
                if indiv[1].alive is True and indiv[0] not in fam[1].husband_id or indiv[0] not in fam[1].wife_id:
                    if Individual.calculate_age(indiv[1]) > 30:
                        alive_single.add(indiv[0])
                    else:
                        print("NOTICE: INDIVIDUAL: US31: {}: is alive and single and less than 30 years old".format(
                            indiv[0]))

        return alive_single != []
