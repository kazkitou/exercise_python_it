'''Project Euler Problem 44'''
import itertools

def problem_44() -> int:
    '''Pentagon numbers'''
    # n が増加するほど差が増加するため n項とn+1項が最も最小となる差をとることになる
    for j in itertools.count(1):
        sum_num = get_pentagonal_number(j) + get_pentagonal_number(j+1)
        diff_num = get_pentagonal_number(j+1) - get_pentagonal_number(j)
        print(j, sum_num, diff_num)
        if judge_pentagonal_number(sum_num) and judge_pentagonal_number(diff_num):
            return diff_num
    return -1

def get_pentagonal_number(index: int) -> int:
    '''
        五角数は Pn = n(3n-1)/2 で生成される。
        最初の10項は
            1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
        引数index項の値を返す。
    '''
    return (index*(3*index -1)) / 2

def judge_pentagonal_number(num: int) -> bool:
    '''
        引数が五角数であるか判断する。
            True  -> 五角数である
            False -> 五角数でない
    '''
    for i in itertools.count(1):
        check_num = get_pentagonal_number(i)
        if check_num == num:
            return True
        if i > num:
            break
    return False

if __name__ == '__main__':
    print(problem_44())
