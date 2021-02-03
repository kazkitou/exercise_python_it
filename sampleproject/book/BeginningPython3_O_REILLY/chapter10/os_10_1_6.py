import os

os.link('oops.txt', 'yikes.txt')
os.path.isfile('yikes.txt')

os.symlink('oops.txt', 'jeepers.txt')
os.path.isfile('jeepers.txt')
