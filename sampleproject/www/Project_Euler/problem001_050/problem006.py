'''Project Euler Problem 6'''

def problem_6() -> int:
    '''	Sum square difference'''
    calc1 = [num**2 for num in range(1, 101)]
    calc2 = [range(1, 101)]
    return sum(calc2)**2 - sum(calc1)

if __name__ == '__main__':
    print(problem_6())
