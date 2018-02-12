"""
Class to represent an Individual based on GEDCOM Data
"""
import datetime


class Individual:
    __slots__ = "id", "name", "gender", "birthday", "age", "alive", "death", "child", "spouse"

    def __init__(self, unique_id):
        self.id = unique_id
        self.child = {}
        self.spouse = {}
        self.age = ""
        self.birthday = ""
        self.alive = True
        self.death = "NA"

    def set_birthday(self, birthday):
        if Individual.verify_birthday(birthday):
            self.birthday = birthday
        else:
            print(birthday, " is over 150 years ago.")

    def set_age(self):
        self.age = self.calculate_age()

    @staticmethod
    def verify_birthday(date):
        """
        Verify birthday is less than 150 years
        :param date: DY MON YEAR
        :return: True if the birthday is valid and larger than the year 150 years ago.
        """
        year = int(date.split()[2])
        month = int(date.split()[1])
        day = int(date.split()[0])
        birthday = datetime.date(year, month, day)
        today = datetime.datetime.now()
        year_sub = today.year - 150
        today_minus_years = datetime.datetime(year=year_sub,month=month,day=day)

        if birthday.year > today_minus_years.year:
           return (birthday.year > today_minus_years.year) 

        elif birthday.year < today_minus_years.year:
           return (birthday.year < today_minus_years.year)

        elif birthday.year == today_minus_years.year:
           return (birthday.year == today_minus_years.year) 

	
        elif birthday.year != today_minus_years.year:
           return (birthday.year != today_minus_years.year)


    def calculate_age(self):
        """
        Calculate Age Based on Birthday

        :param birthday: DY MON YEAR
        :param death_date: DY MON YEAR
        :return: Integer representation of Age
        """
        birthday = datetime.datetime.strptime(self.birthday, '%d %b %Y')
        if self.death != "NA":
            death_date = datetime.datetime.strptime(self.death, '%d %b %Y')
            return int(abs(death_date.year)) - int(abs(birthday.year))
        today = datetime.datetime.now()
        return int(abs(today.year)) - int(abs(birthday.year))
