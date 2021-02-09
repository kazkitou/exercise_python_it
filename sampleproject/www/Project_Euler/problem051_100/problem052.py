'''Project Euler Problem 52'''
import itertools

def problem_52() -> int:
    '''Permuted multiples'''
    for i in itertools.count(1):
        if judge_permuted_multiples(i, 2, 7):
            return i
    return -1

def judge_permuted_multiples(base: int, mlt_min: int, mlt_max: int) -> bool:
    '''
        引数baseが以下のような置換倍数であるか判断する
        引数mlt_min × base, mlt_min+1 × base, mlt_min+2 × base, ... , mlt_max-1 × base
            True  -> 置換倍数である
            False -> 置換倍数でない
    '''
    for mlt in range(mlt_min, mlt_max):
        if sorted(str(base)) != sorted(str(mlt*base)):
            return False
    return True

if __name__ == '__main__':
    print(problem_52())
