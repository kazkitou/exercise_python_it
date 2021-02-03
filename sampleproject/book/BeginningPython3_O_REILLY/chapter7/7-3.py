import unicodedata

mystery = '\U0001f4a9'
pop_bytes = mystery.encode('utf-8')
print('pop_bytes = ' + str(pop_bytes))

pop_string = pop_bytes.decode()
print('   mystery = ' + str(mystery))
print('pop_string = ' + pop_string)