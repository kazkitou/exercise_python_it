'''Project Euler Problem 14'''

def problem_14() -> int:
    '''Longest Collatz sequence'''
    ret = 0
    max_len = 0
    for i in range(2, 1000000):
        tmp_list = []
        tmp_list.append(i)
        tmp = i
        while tmp != 1:
            tmp = collatz_problem(tmp)
            tmp_list.append(tmp)
        if len(tmp_list) > max_len:
            max_len = len(tmp_list)
            ret = i
    return ret

def collatz_problem(num: int) -> list:
    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1

if __name__ == '__main__':
    print(problem_14())
