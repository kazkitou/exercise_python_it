from datetime import datetime

today_string = ''
with open('today.txt', 'rt') as fp:
    today_string = fp.read()

print(today_string)