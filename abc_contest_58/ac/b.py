O = input()
E = input()

password = ""
for o, e in zip(O, E):
    password += o + e

if len(O) - len(E) == 1:
    password += O[-1]

print(password)
