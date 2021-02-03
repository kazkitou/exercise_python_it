import multiprocessing
import random
from datetime import datetime
import time
from typing import NoReturn

def exec_method(name: str) -> NoReturn:
    print(name + ' start')
    start = datetime.now().second
    time.sleep(random.choice([1,2,3,4,5]))
    end = datetime.now().second
    print(name + ' end :'+str(end - start)+' 秒')

if __name__ == "__main__":
    print('main process')
    for i in range(3):
        p = multiprocessing.Process(target=exec_method, args=('    process {}'.format(i),))
        p.start()