from datetime import datetime

today_string = ''
with open('today.txt', 'rt') as fp:
    today_string = fp.read()

import time
print(time.strptime(today_string, '%Y-%m-%d'))