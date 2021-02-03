'''Project Euler Problem 44'''
import itertools
import math

def problem_44() -> int:
    '''Pentagon numbers'''
    # どういうアルゴリズムにすればよいか分からない
    # Pnの五角数 から 項nを減算していき、算出した結果が最小の差になると仮定した
    for j in itertools.count(1):
        j_num = get_pentagonal_number(j)
        for k in range(j-1, 0, -1):
            k_num = get_pentagonal_number(k)
            if judge_pentagonal_number(j_num + k_num) and judge_pentagonal_number(j_num - k_num):
                return j_num - k_num
    return -1

def get_pentagonal_number(num_n: int) -> int:
    '''
        五角数は Pn = n(3n-1)/2 で生成される。
        最初の10項は
            1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
        引数num_n項の値を返す。
    '''
    return (num_n*(3*num_n - 1)) / 2

def judge_pentagonal_number(num: int) -> bool:
    '''
        引数が五角数であるか判断する。
            True  -> 五角数である
            False -> 五角数でない
                n(3n - 1) / 2 = k
                n(3n - 1) / 2 - k = 0
                3n**2 -n - 2k = 0
                n = (1±√1+24k) / 6
                nが正の整数であれば五角数であると判断する。
                （±については+で考える）... ±を-で考えるとnが負の値になるため
    '''
    return ((1+math.sqrt(1+24*num))/6).is_integer()

if __name__ == '__main__':
    print(problem_44())
