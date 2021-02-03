''' pylint test. '''
from datetime import date
from datetime import timedelta
from datetime import time
from datetime import datetime

halloween = date(2014, 10, 31)

print('hallowween ------------------> ' + str(halloween))
print('hallowween day --------------> ' + str(halloween.day))
print('hallowween month ------------> ' + str(halloween.month))
print('hallowween year -------------> ' + str(halloween.year))
print('hallowween(ISO 8601 Format) -> ' + str(halloween.isoformat()))

now = date.today()
print('today ----------> ' + str(now))

one_day = timedelta(days=1)
tomorrow = now + one_day
print('tomorrow -------> ' + str(tomorrow))

nowPlus17days = now + one_day*17
print('today + 17days -> ' + str(nowPlus17days))

yesterday = now - one_day
print('yesterday ------> ' + str(yesterday))

noon = time(12, 0, 0)
print('noon -------------> ' + str(noon))
print('noon.hour --------> ' + str(noon.hour))
print('noon.minute ------> ' + str(noon.minute))
print('noon.second ------> ' + str(noon.second))
print('noon.microsecond -> ' + str(noon.microsecond))

some_day = datetime(2014, 1, 2, 3, 4, 5, 6)
print('some day ------------------> ' + str(some_day))
print('some day(ISO 8601 Format) -> ' + str(some_day.isoformat()))

now = datetime.now()
print('today -------------> ' + str(now))
print('today year --------> ' + str(now.year))
print('today month -------> ' + str(now.month))
print('today day ---------> ' + str(now.day))
print('today.hour --------> ' + str(now.hour))
print('today.minute ------> ' + str(now.minute))
print('today.second ------> ' + str(now.second))
print('today.microsecond -> ' + str(now.microsecond))
