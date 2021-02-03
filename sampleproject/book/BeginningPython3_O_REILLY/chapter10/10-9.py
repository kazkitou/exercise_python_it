from datetime import datetime, timedelta

birth_day = datetime(1987, 8, 9).date()
print(birth_day)

fmt = 'year = %Y , month = %B , day = %d , day of week = %A'
print(birth_day.strftime(fmt))

delta_days = timedelta(days=1)*10000
after_birth = birth_day + delta_days
print("[Birth day + {} days] -> {}".format(str(delta_days.days), str(after_birth.strftime(fmt))))
