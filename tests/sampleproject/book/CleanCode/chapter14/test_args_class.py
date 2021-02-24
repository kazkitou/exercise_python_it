import pytest, sys, pathlib

if not str(pathlib.Path.cwd()) in sys.path:
    sys.path.append(str(pathlib.Path.cwd()))
from sampleproject.book.CleanCode.chapter14 import args_class


def test___init__():
    try:
        args = [True, 2, "three"]
        arg = args_class("l,p# ,d*".format(args))
        logging = arg.get_boolean("l")
        port = arg.get_int("p")
        directory = arg.get_string("d")
        execute_application(logging, port, directory)
    except Exception as e:
        print("引数エラー：{}".format(e.error_message()))


if __name__ == "__main__":
    pass
