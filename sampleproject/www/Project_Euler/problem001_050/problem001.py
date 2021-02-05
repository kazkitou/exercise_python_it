'''Project Euler Problem 1'''

def problem_1() -> int:
    '''Multiples of 3 and 5'''
    ret = sum(filter(lambda num: (num % 3 == 0) or (num % 5 == 0), range(1000)))
    return ret

if __name__ == '__main__':
    print(problem_1())
