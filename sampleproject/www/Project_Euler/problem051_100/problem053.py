'''Project Euler Problem 53'''

def problem_53() -> int:
    '''Combinatoric selections'''
    counter = 0
    for n_num in range(1, 101):
        for r_num in range(1, n_num):
            # nCrが100万を超える組み合わせを数える
            if get_combination_pattertn(n_num, r_num) > 1000000:
                counter += 1
    return counter

def get_combination_pattertn(n_num: int, r_num: int) -> int:
    '''nCrを返す'''
    if n_num < 1 or r_num < 1 or n_num < r_num:
        return 0
    div_child = get_factorial_pattertn(n_num)
    div_mother = get_factorial_pattertn(r_num) * get_factorial_pattertn(n_num - r_num)
    return div_child / div_mother

def get_factorial_pattertn(n_num: int) -> int:
    '''n!を返す'''
    if n_num == 0:
        return 1
    return n_num * get_factorial_pattertn(n_num-1)

if __name__ == '__main__':
    print(problem_53())
