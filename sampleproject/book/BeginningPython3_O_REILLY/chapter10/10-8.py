from datetime import date

birth_day = date(1987, 8, 9)
print(birth_day)

fmt = "year = %Y , month = %B , day = %d , day of the week = %A"
print(birth_day.strftime(fmt))
