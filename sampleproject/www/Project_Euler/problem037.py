'''Project Euler Problem 37'''
import itertools
import math

def problem_37() -> int:
    '''Truncatable primes'''
    count = 0
    palindrome = 0
    for i in itertools.count(11, 2):
        if judge_prim_number(i) and\
            judge_left_cutting_back_possibility_prime_number(i) and\
            judge_right_cutting_back_possibility_prime_number(i):
            count += 1
            palindrome += i
        if count >= 11:
            break
    return palindrome

def judge_prim_number(num: int) -> bool:
    '''
        引数numが素数であるか判断する。
            True  -> 素数である
            False -> 素数でない
    '''
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def judge_left_cutting_back_possibility_prime_number(num: int) -> bool:
    '''
        引数numが左の桁を切り詰めた値も素数であるか判断する。
            True  -> 切り詰めた場合に素数である
            False -> 切り詰めた場合に素数でない
            ex)  引数num = 3797 -> (3797, 797, 97, 7)
    '''
    if num < 2:
        return False
    while num != 0:
        if not judge_prim_number(num):
            return False
        num %= int(math.pow(10, len(str(num))-1))
    return True

def judge_right_cutting_back_possibility_prime_number(num: int) -> bool:
    '''
        引数numが右の桁を切り詰めた値も素数であるか判断する。
            True  -> 切り詰めた場合に素数である
            False -> 切り詰めた場合に素数でない
            ex)  引数num = 3797 -> (3797, 379, 37, 3)
    '''
    if num < 2:
        return False
    while num != 0:
        if not judge_prim_number(num):
            return False
        num //= 10
    return True

if __name__ == '__main__':
    print(problem_37())
