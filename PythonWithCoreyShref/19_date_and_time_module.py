# how to work with dates with in python
# using every type of application datetime, datetimes, timezones, timedeltas, 

import datetime
import pytz

# datetime.date()
d = datetime.date(2024,10,24)
print(d)

# find out today()
tday = datetime.date.today()
print(tday)

print(tday.weekday())
print(tday.isoweekday())

# monday 0 sunday 6         weekday sunday is 6
# monday 1 sunday 7         isoweekday sunday is 7

# Time deltas difference between two dates or times

tdelta =  datetime.timedelta(days = 7)
print(tday + tdelta)

print(tday - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2025, 3, 8)
till_bday = bday - tday
print(till_bday.days) # get days
print(till_bday.total_seconds()) # total number seconds

# datetime.time working on hours, minutes, seconds and microseconds
t = datetime.time(8,27, 00,100000)
print(t)

print(t.hour)

dt = datetime.datetime(2024, 10, 6, 8, 28, 00, 000000)
print(dt.date())
print(dt.time())

tdelta = datetime.timedelta(days=7)
print(dt+tdelta)

tdelta = datetime.timedelta(hours=7)
print(dt+tdelta)

# usefull constructors

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today) # return current local datetime with time zone none
print(dt_now) # gives an option passing an timezone
print(dt_utcnow) # 

# installing pytz pytz is large set of timezones.

dt = datetime.datetime(2024, 10, 6, 8, 37, 45, tzinfo=pytz.UTC)
print(dt)

dt_now =datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_now)

# convert UTC time to local time
dt_mtn = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_mtn)

print(dt_mtn.isoformat())
# # nowdt = datetime.now(dt_mtn)

# todaydt = datetime(2012,6,15,tzinfo=dt_mtn)

# print(todaydt)

for tz in pytz.all_timezones:
    print(tz)
    
print(dt_mtn.strftime('%d %B %Y'))