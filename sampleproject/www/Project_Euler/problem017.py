'''Project Euler Problem 17'''

def problem_17() -> int:
    '''Number letter counts'''
    # 再起処理を使うことでもっとコードを短くできそう
    max_len = 0
    for i in range(1, 1001):
        tmp_char = get_natural_lang_xxxx(i)
        tmp_char = tmp_char.replace(' ', '')
        tmp_char = tmp_char.replace('-', '')
        max_len += len(tmp_char)
    return max_len

def get_natural_lang_x(num: int) -> str:
    '''自然言語 数字1桁'''
    lang = ''
    natural_lang = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if num < 10:
        lang = natural_lang[num]
    return lang

def get_natural_lang_xx(num: int) -> str:
    '''自然言語 数字2桁'''
    lang = ''
    natural_lang = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    natural_lang_x0 = ['ten', 'twenty', 'thirty', 'forty',
                        'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if num < 10:
        lang = get_natural_lang_x(num)
    elif num < 20:
        lang = natural_lang[num - 10]
    elif (num < 100) and (num % 10 == 0):
        lang = natural_lang_x0[(num // 10) -1]
    elif num < 100:
        str_num = '{:0>4}'.format(num)
        # abcd  :   数値の4桁表示（足りない桁は0埋め）
        #   keta  = a   b   c   d
        #   index = 0   1   2   3
        for keta in range(2, 4):
            if keta == 3:
                lang += get_natural_lang_x(int(str_num[keta]))
            else:
                lang += natural_lang_x0[(num // 10) -1]
                if str_num[keta] != '0':
                    lang += '-'
    else:
        lang = ''

    return lang

def get_natural_lang_xxx(num: int) -> str:
    '''自然言語 数字3桁'''
    lang = ''
    if num < 100:
        lang = get_natural_lang_xx(num)
    elif num < 1000:
        str_num = '{:0>4}'.format(num)
        # abcd  :   数値の4桁表示
        #   keta  = a   b   c   d
        #   index = 0   1   2   3
        if str_num[1] != '0':
            lang = get_natural_lang_x(int(str_num[1])) + ' hundred'
            if str_num[2:4] != '00':
                lang = lang + ' and ' + get_natural_lang_xx(int(str_num[2:4]))
    else:
        lang = ''

    return lang

def get_natural_lang_xxxx(num: int) -> str:
    '''自然言語 数字4桁'''
    lang = ''
    if num < 1000:
        lang = get_natural_lang_xxx(num)
    else:
        # 問題文から、1000以外の考慮不要
        lang = 'one thousand'
    return lang

def recursion_en_num_lang(num: int) -> str:
    '''
        上記処理を再帰を用いたバージョン
    '''
    en_num_lang = [
        'zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
        'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
        ]
    en_num_lang_x0 = [
        '' , '', 'twenty', 'thirty', 'forty',
        'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
        ]
    lang = ''
    if num < 20:
        lang = en_num_lang[num]
    elif num < 100:
        lang = en_num_lang_x0[num // 10]
        if num % 10 != 0:
            lang += '-' + recursion_en_num_lang(num % 10)
    elif num < 1000:
        lang = en_num_lang[num // 100] + ' handred'
        if num % 100 != 0:
            lang += ' and ' + recursion_en_num_lang(num % 100)
    elif num < 10000:
        lang = en_num_lang[num // 1000] + ' thousand'
        if num % 1000 != 0:
            lang += ' and ' + recursion_en_num_lang(num % 1000)
    else:
        lang = 'No exist case'

    return lang

if __name__ == '__main__':
    print(problem_17())
#   以下、再帰処理を用いたバージョン
#    max_len = 0
#    for i in range(1, 1001):
#        tmp_str = recursion_en_num_lang(i)
#        tmp_str = tmp_str.replace(' ', '')
#        tmp_str = tmp_str.replace('-', '')
#        max_len += len(tmp_str)
#    print(max_len)
