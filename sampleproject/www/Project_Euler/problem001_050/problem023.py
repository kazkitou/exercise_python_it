'''Project Euler Problem 23'''

def problem_23() -> int:
    '''Non-abundant sums'''
    # 過剰数のリストを作成する
    abundant_num_list = []
    for num in range(1, 28123):
        if judge_abundant_number(num):
            abundant_num_list.append(num)

    # 28123までの2つの過剰数の和を作成する
    abundant_num_sum_list = set()
    for left_num in abundant_num_list:
        for right_num in abundant_num_list:
            if left_num + right_num > 28123:
                break
            abundant_num_sum_list.add(left_num + right_num)

    # 28123までの数字で、2つの過剰数の和で表せない数の和を作成する
    ret = 0
    for num in range(1, 28123):
        if not num in abundant_num_sum_list:
            ret += num

    return ret

def judge_abundant_number(num: int) -> bool:
    '''
        過剰数かどうか判断する。
            True  -> 過剰数である
            False -> 過剰数でない
    '''
    sum_div_num = sum(filter(lambda cnt : num % cnt == 0, range(1, num)))
    if sum_div_num > num:
        return True
    return False

if __name__ == '__main__':
    print(problem_23())
