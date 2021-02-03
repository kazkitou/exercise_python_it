'''Project Euler Problem 46'''
import itertools
import math

def problem_46() -> int:
    '''Goldbach's other conjecture'''
    for i in itertools.count(34):
        if not judge_oddly_integrated_number(i):
            continue
        if not judge_goldbach_other_conjecture(i):
            return i
    return -1

def judge_goldbach_other_conjecture(num: int) -> bool:
    '''
        全ての奇合成数は平方数の2倍と素数の和で表せると予想
            奇合成数 .. 1と自身以外に約数をもち、その約数が全て奇数である整数
            平方数 .... 自然数の2乗
                奇合成数 = 素数 + 自然数の2乗 * 2
            引数num から自然数の2乗 * 2を引いた値が素数であれば、予想通りとみなす
    '''
    for j in itertools.count(1):
        check_num = num - j**2 * 2
        if check_num <= 0:
            break
        if judge_prim_number(check_num):
            return True
    return False

def judge_prim_number(num: int) -> bool:
    '''
        素数であるか判断する。
            True  -> 素数である
            False -> 素数でない
    '''
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def judge_oddly_integrated_number(num: int) -> bool:
    '''
        引数numが奇合成数か判断する
            True  -> 奇合成数である
            False -> 奇合成数でない
    '''
    return judge_oddly_list(get_factor(num))

def get_factor(num: int) -> list:
    '''
        引数numの約数を返す
        （1と引数num自身を除く）
    '''
    factors = list()
    for i in range(2, num//2+1):
        if num % i == 0:
            factors.append(i)
    return factors

def judge_oddly_list(check_list: list) -> bool:
    '''
        引数check_list内の数字が全て奇数か判断する
            True  -> 全て奇数である
            False -> 偶数が含まれる
    '''
    if len(check_list) == 0:
        return False

    for num in check_list:
        if num % 2 == 0:
            return False
    return True

if __name__ == '__main__':
    print(problem_46())
