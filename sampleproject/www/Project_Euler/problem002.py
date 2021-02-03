'''Project Euler Problem 2'''

def problem_2() -> int:
    '''Even Fibonacci numbers'''
    fibnacci_array = [1, 2]
    while fibnacci_array[-1] < 4000000:
        fibnacci_array.append(fibnacci_array[-1] + fibnacci_array[-2])
    ret = sum(filter(lambda num: (num % 2 == 0), fibnacci_array))
    return ret

if __name__ == '__main__':
    print(problem_2())
