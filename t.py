import datetime
date='2018 1 5'
print (date.split())
year = int(date.split()[0])
month = int(date.split()[1])
day = int(date.split()[2])
birthday = datetime.date(year, month, day)

today = datetime.datetime.now()
print (today)
year_sub = today.year - 150
print (today.year)
print (year_sub)
today_minus_years = datetime.datetime(year=year_sub,month=month,day=day)
print (birthday.year == today_minus_years.year)
