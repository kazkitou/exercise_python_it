def get_odds(first=None, last=None, step=None):

    if first == None:
        first = 0
    if last == None:
        last = 10
    if step == None:
        step = 1

    for elm in range(first, last, step):
        if elm % 2 == 1:
            yield elm


odds_list = [odd for odd in get_odds()]
print(odds_list)

count = 0
for elm in get_odds():
    count += 1
    if count == 3:
        print(elm)
