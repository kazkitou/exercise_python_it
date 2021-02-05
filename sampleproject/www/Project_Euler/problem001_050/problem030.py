'''Project Euler Problem 30'''
import math

def problem_30() -> int:
    '''Distinct powers'''
    max_num = int(math.pow(9, 5)) * 4
    ret_list = list()
    for i in range(2, max_num):
        if judge_num_5jo(i):
            ret_list.append(i)
    return sum(ret_list)

def judge_num_5jo(num: int) -> bool:
    '''
        引数numが各桁を5乗した値と一致するか確認する
            True  -> 一致する
            False -> 一致しない
    '''
    num_str = str(num)
    sum_num = 0
    for keta in num_str:
        sum_num += int(math.pow(int(keta), 5))
    if num == sum_num:
        return True
    return False


if __name__ == '__main__':
    print(problem_30())
