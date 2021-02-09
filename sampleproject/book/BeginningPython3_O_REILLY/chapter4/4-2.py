if __name__ == "__main__":
    guess_me = int(input("input int guess_me = "))
    start = int(input("input int start = "))
    while True:
        if start < guess_me:
            print("too low")
        elif start == guess_me:
            print("found it!")
        else:
            print("oops")
            break
        start += 1
