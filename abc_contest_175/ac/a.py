s = input()
if s == 'RRR':
    print(3)
elif s == 'RRS' or s == 'SRR':
    print(2)
elif 'R' in s:
    print(1)
else:
    print(0)
