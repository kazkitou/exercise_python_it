test1 = "This is atest of the emergency test system"
with open("test.txt", "w") as fp:
    fp.write(test1)

test2 = ""
with open("test.txt", "r") as fp:
    test2 = fp.read()

print("test1 = " + test1)
print("test2 = " + test2)

if test1 == test2:
    print("test1 Equal test2")
else:
    print("test1 Not Equal test2")