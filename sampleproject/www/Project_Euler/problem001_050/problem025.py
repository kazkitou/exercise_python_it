"""Project Euler Problem 25"""


def problem_25() -> str:
    """1000-digit Fibonacci number"""
    print("F_11 = {: >3}".format(get_fibonacci_number(11)))
    print("F_12 = {: >3}".format(get_fibonacci_number(12)))
    cnt = 13
    while True:
        fib_num = str(get_fibonacci_number(cnt))
        if len(fib_num) >= 1000:
            break
        cnt += 1

    return cnt


def get_fibonacci_number(num: int) -> int:
    """
    F_n = F_n-1 + F_n-2
        [note]  F_1 = 1, F_2 = 1)
    """
    if num < 3:
        return 1

    array = [1, 1]
    i = 3
    while i <= num:
        n_minus2 = array.pop(0)
        n_minus1 = array[0]
        array.append(n_minus1 + n_minus2)
        i += 1
    return array[1]


if __name__ == "__main__":
    print(problem_25())
