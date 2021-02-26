import sys, pathlib, subprocess

if not str(pathlib.Path.cwd()) in sys.path:
    sys.path.append(str(pathlib.Path.cwd()))
from sampleproject.book.CleanCode.chapter14 import args_class


def args_main(*args):
    try:
        arg = args_class("l,p# ,d*", *args)
        logging = arg.getBoolean("l")
        port = arg.getInt("p")
        directory = arg.getString("d")
        result = subprocess.run([logging, port, directory]).stdout.decode("utf-8")
    except Exception as e:
        result = "引数エラー：{}".format(e.error_message())
    return result


if __name__ == "__main__":
    args_main()
