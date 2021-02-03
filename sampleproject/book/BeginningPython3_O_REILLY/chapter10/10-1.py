from datetime import datetime
import os

if os.path.exists('today.txt'):
    os.remove('today.txt')

with open('today.txt', 'wt') as fp:
    fp.write(str(datetime.now().date()))