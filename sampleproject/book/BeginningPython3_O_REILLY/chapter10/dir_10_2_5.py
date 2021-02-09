import glob

print(glob.glob("poems/m*"))
print(glob.glob("poems/??"))
print(glob.glob("poems/m??????e"))
print(glob.glob("poems/[klm]*e]"))
