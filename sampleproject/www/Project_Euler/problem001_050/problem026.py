'''Project Euler Problem 26'''

def problem_26() -> int:
    '''Reciprocal cycles'''
    max_d = 1000
    max_cycle_len = 0
    max_cycle_val = 0
    for i in range(3, max_d, 2):
        cycle_len = get_reciprocal_cycles_length(i)
        if max_cycle_len < cycle_len:
            max_cycle_len = cycle_len
            max_cycle_val = i
    return max_cycle_val

def get_reciprocal_cycles_length(num: int) -> int:
    '''
        引数numの循環節の長さを返す。
            割り算した際の余りが同じ -> 以降の計算結果が循環すると考える
    '''
    cycle_len = 0
    remainder = 1
    remainder_list = list()
    while True:
        remainder = remainder % num
        if remainder in remainder_list:
            break
        remainder_list.append(remainder)
        remainder *= 10
    cycle_len = len(remainder_list) - remainder_list.index(remainder)
    return cycle_len

if __name__ == '__main__':
    print(problem_26())
