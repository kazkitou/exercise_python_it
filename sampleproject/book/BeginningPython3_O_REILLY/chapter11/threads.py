import threading


def do_this(what):
    whoami(what)


def whoami(what):
    print("Thread {} says: {}".format(threading.current_thread(), what))


if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this, args=("I'm function {}".format(n),))
        p.start()
