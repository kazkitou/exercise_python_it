'''Project Euler Problem 47'''
import itertools

def problem_47() -> int:
    '''Distinct primes factors'''
    serial_num = 4
    multiple_prime_factor_list = list()
    for i in itertools.count(647):
        multiple_prime_factor_list.append(
            get_multiple_prime_factor_decomposition(get_prime_factor_decomposition(i)))
        if len(multiple_prime_factor_list[-1]) != serial_num:
            multiple_prime_factor_list.clear()
        if len(multiple_prime_factor_list) == serial_num:
            return i - (serial_num - 1)
    return -1

def get_multiple_prime_factor_decomposition(prime_factor: dict) -> set:
    '''
        引数prime_factor（素因数分解を辞書形式でまとめた結果）から累乗を除いて掛け算の形で返す
            それぞれ3つの異なる素因数を持つ連続する3つの数が最初に現れるのは:
                644 = 2^2 × 7 × 23
                645 = 3   × 5 × 43
                646 = 2   × 17 × 19
            上記説明があるため、単純に素因数分解結果の底の種類を数えるだけではダメなので、累乗の計算結果を返す
    '''
    multiple_prime_factor = set()
    for base_num in prime_factor.keys():
        multiple_prime_factor.add(base_num ** prime_factor[base_num])
    return multiple_prime_factor

def get_prime_factor_decomposition(num: int) -> dict:
    '''
        引数numの素因数分解した結果を辞書型で返す
    '''
    prim_factor_list = dict()
    div_num = 2
    while num > 1:
        if num % div_num == 0:
            prim_factor_list[div_num] = prim_factor_list.get(div_num, 0) + 1
            num //= div_num
        else:
            div_num += 1
    return prim_factor_list

if __name__ == '__main__':
    print(problem_47())
