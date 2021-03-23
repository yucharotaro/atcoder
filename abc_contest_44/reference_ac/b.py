a = input()
for x in set(a):
    if a.count(x) & 1:
        print('No')
        exit()
print('Yes')
