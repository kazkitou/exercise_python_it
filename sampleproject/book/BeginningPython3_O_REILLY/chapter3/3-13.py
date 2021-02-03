e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
f2e ={}
for key, val in e2f.items():
    f2e[val] = key
print(f2e['chien'])