'''Project Euler Problem 10'''

def problem_10() -> int:
    '''Summation of primes'''
    prim_num_list = [2]
    check_max = 2000000
    # 素数かどうか、3から順に判断する。
    # 偶数は素数ではないため、step 2を指定する。
    for i in range(3, check_max+1, 2):
        if judge_prim_number(i):
            prim_num_list.append(i)

    return sum(prim_num_list)

def judge_prim_number(num: int) -> bool:
    '''Judge Prim Number'''
    for i in range(2, num):
        if i**2 > num:
            break
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(problem_10())
