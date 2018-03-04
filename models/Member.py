import datetime


class Member:

    @staticmethod
    def verify_date_not_future(obj_id, date, member_type):
        if date == "NA":
            return False
        today = datetime.datetime.today()
        formatted_date = datetime.datetime.strptime(date, '%d %b %Y')
        if formatted_date > today:
            print(
                "ERROR: {}: US01: {}: {} is in the future from {}".format(
                    member_type, obj_id, formatted_date.strftime("%m %d %Y"), today.strftime("%m %d %Y")))
            return formatted_date
        return False

    @staticmethod
    def verify_date_150_years(date):
        """
        Verify date is less than 150 years ago
        :return: True if the date is valid and bigger than the year 150 years ago.
        """
        formatted_date = datetime.datetime.strptime(date, '%d %b %Y')
        today = datetime.datetime.now()
        year_sub = today.year - 150
        today_minus_years = datetime.datetime(year=year_sub, day=today.day, month=today.month)
        return formatted_date.year > today_minus_years.year

    @staticmethod
    def return_upcoming_date(date, today=datetime.datetime.now()):
        """
        Prints whether this date is upcoming
        :return: date object if date is upcoming within 30 days
        """
        current_year_date_str = datetime.datetime.strptime(date, '%d %b %Y').strftime(
            "%m %d") + " " + str(today.year)
        current_year_date = datetime.datetime.strptime(current_year_date_str, '%m %d %Y')
        delta_from_date = current_year_date - today
        return 0 <= delta_from_date.days <= 30
