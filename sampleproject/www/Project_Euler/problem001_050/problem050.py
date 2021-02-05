'''Project Euler Problem 50'''
import math

def problem_50() -> int:
    '''Consecutive prime sum'''
    # 素数の合計した値が素数である数字で1000000未満の最大値を求める
    #   ex) 素数 = 2, 3, 5, ...
    #       項1 = [2]                  : 合計 2    == 素数
    #       項2 = [2, 3]               : 合計 5    == 素数
    #       項3 = [2, 3, 5]            : 合計 10   != 素数
    #       ...
    #       項6 = [2, 3, 5, 7, 11, 13] : 合計 41   == 素数
    #       ...
    #       項z = [2, 3, ..., zzzz]    : 合計 ZZZZ == 素数  (ZZZZ < 1000000)
    #       項y = [2, 3, ..., yyyy]    : 合計 YYYY != 素数  (YYYY < 1000000)
    #       項x = [2, 3, ..., xxxx]    : 合計 XXXX == 素数  (XXXX > 1000000)
    #           ※ y=z+1, x=y+1, ZZZZ < YYYY < 1000000 < XXXX
    #       上記のZZZZを求める。YYYYは合計値が素数でないため対象外
    prim_num_list = list()
    sum_prim_num_list = list()
    check_sum_p_num = 0
    for check_p_num in range(2, 1000000):
        if judge_prim_number(check_p_num):
            prim_num_list.append(check_p_num)
            check_sum_p_num = sum(prim_num_list)
            if judge_prim_number(check_sum_p_num):
                sum_prim_num_list.append(check_sum_p_num)
                if sum_prim_num_list[-1] > 1000000:
                    return sum_prim_num_list[-2]
    return -1

def judge_prim_number(num: int) -> bool:
    '''
        引数numが素数かどうか判断する
            True  -> 素数である
            False -> 素数でない
    '''
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(problem_50())
