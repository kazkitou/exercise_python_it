elm_list = {"name": "Hydrogen", "symbol": "H", "number": 1}


class Elements:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.symbol, self.number)

    @property
    def get_name(self):
        return self.__name

    @property
    def get_symbol(self):
        return self.__symbol

    @property
    def get_number(self):
        return self.__number


hydrogen = Elements(**elm_list)
print(hydrogen.get_name, hydrogen.get_symbol, hydrogen.get_number)
