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
