if __name__ == "__main__":
    guess_me = int(input("input int guess_me = "))
    if guess_me < 7:
        print("too low")
    elif guess_me > 7:
        print("too high")
    else:
        # guess_me == 7
        print("just right")
