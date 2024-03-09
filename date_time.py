# dates ,times ,deltas and times zones

import datetime as dt
print(dt.datetime.now()) # print currend time and date
print(dt.datetime.now().date()) # print time date
print(dt.date.today()) # print date only
print(dt.datetime.now().time()) # print time only

# date delta

date1 = dt.date.today()
date2 = dt.timedelta(days=4)
print(date1)
print(date1 - date2) # difference

date1 = dt.date(2024,1,1)
date2 = dt.datetime.now().date()
print(date2 - date1)

# time zone

import pytz

dt1 = dt.datetime.now()
print(dt1)
dt2 = dt.timezone.now(pytz.utc)
print(dt2)



# Get the current time in Sweden

sweden_timezone = pytz.timezone('Europe/Stockholm')
sweden_time = dt.now(sweden_timezone)
print(sweden_time)