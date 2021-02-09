elm_list = {"name": "Hydrogen", "symbol": "H", "number": 1}


class Elements:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


hydrogen = Elements(**elm_list)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)
