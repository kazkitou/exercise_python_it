''' 自作デコレータ '''
from pprint import pprint

def my_decorator_func_s_r_e(func):
    ''' 自作デコレータ 関数　開始、戻り値、終了 '''
    def my_wrap(*args, **kwargs):
        print('start {}'.format(func.__name__))
        ret = func(*args, **kwargs)
        pprint('{} return = {}'.format(func.__name__, ret))
        return ret
    return my_wrap
