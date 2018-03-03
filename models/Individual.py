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
  
    def validate_spouse(self, id):
          
          if id in self.child:
                print("ERROR: INDIVIDUAL: US17: {}: Marriage cannot happen with descendants: {}.".format(self.id,
                                                                                                 id))
                return False
          return True
    
    def birth_before_death(self):
        """
        US 03: Validate birth occurs before death
        :return: True if birth occurs before death
        """
        birthday = datetime.datetime.strptime(self.birthday, '%d %b %Y')
        if self.death != "NA":
            death_date = datetime.datetime.strptime(self.death, '%d %b %Y')
            if death_date < birthday:
                print("ERROR: INDIVIDUAL: US03: Individual {}: {}'s Birthday on {} occurs after death date on {}.".format(self.id,
                                                                                       self.name,self.birthday, self.death))
                return False
        return True  
