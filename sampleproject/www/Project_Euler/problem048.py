'''Project Euler Problem 48'''

def problem_48() -> str:
    '''Self powers'''
    sum_self_powers = 0
    for i in range(1, 1001):
        sum_self_powers += i**i
        sum_self_powers = sum_self_powers % 10**10
    return sum_self_powers

if __name__ == '__main__':
    print(problem_48())
