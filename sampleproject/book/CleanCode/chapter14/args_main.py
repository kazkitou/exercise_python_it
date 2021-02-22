import args_class

def args_main(*args):
    try:
        arg = args_class("l,p# ,d*", *args)
        logging = arg.getBoolean("l")
        port = arg.getInt("p")
        directory = arg.getString("d")
        executeApplication(logging, port, directory)
    except Exception as e:
        print("引数エラー： {}".format(e))


if __name__ == "__main__":
    args_main()
