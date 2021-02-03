import time
def test(func) :
    def wapper(*args, **kwargs) :
        print("start")
        start_time = time.time_ns()
        result = func(*args, **kwargs)
        end_time = time.time_ns()
        print('計測時間 = '+str(end_time-start_time)+r' [ナノ秒]')
        print('end')
        return result
    return wapper

@test
def my_func(start, last) :
    START = 0
    END = 10
    for cnt in range((END+1)) :
        if cnt == START :
            print(start)
        elif cnt == END :
            print(last)

my_func('自作関数の最初から', '最後までの時間計測')
