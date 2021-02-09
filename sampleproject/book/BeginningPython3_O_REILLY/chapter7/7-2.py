import unicodedata

mystery = "\U0001f4a9"
pop_bytes = mystery.encode("utf-8")

print(pop_bytes)
