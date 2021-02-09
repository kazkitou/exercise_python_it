import os

# 作成予定のものが作成済みであれば削除しておく
# 10.2.2 rmdir()による削除
if os.path.exists("poems/mcintyre/the_good_man"):
    os.remove("poems/mcintyre/the_good_man")
if os.path.exists("poems/mcintyre"):
    os.rmdir("poems/mcintyre")
if os.path.exists("poems"):
    os.rmdir("poems")

# 10.2.3 listdir()による内容リストの作成
os.mkdir("poems")
print(os.listdir("poems"))

os.mkdir("poems/mcintyre")
print(os.listdir("poems"))

with open("poems/mcintyre/the_good_man", "wt") as fp:
    fp.write(
        """Cheerful and happy was his mod,
    He to the poor was kind and good,
    And he oft' times did find them food,
    Also supplies of coal and wood,
    He never spake a word was rude,
    And cheer'd those did o'er sorrows brood,
    He passed away not understood,
    Because no poet in his lays
    Had penned a sonnet in his praise,
    'Tis sad, but such is world's ways.
    """
    )

print(os.listdir("poems/mcintyre"))
