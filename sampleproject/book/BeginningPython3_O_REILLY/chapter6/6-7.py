elm_list = {'name':'Hydrogen', 'symbol':'H', 'number':1}

class Elements():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name, self.symbol, self.number)

hydrogen = Elements(**elm_list)
print(hydrogen)

class Elements2(Elements):
    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.symbol, self.number)

hydrogen = Elements2(**elm_list)
print(hydrogen)
