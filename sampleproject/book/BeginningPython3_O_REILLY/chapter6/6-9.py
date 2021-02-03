class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'

bear = Bear()
rabb = Rabbit()
octo = Octothorpe()

print('Bear eats {}, Rabbit eats {}, Octothorpe eats {}'.format(bear.eats(), rabb.eats(), octo.eats()))