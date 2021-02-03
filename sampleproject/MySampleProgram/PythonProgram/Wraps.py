from pprint import pprint

def my_decorator(func):
    def wrap(*args, **kwargs):
        print('start {}'.format(func.__name__))
        ret = func(*args, **kwargs)
        pprint('{} return = {}'.format(func.__name__, ret))
        return ret
    return wrap