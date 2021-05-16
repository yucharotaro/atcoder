S = input()
maru, hate = [], []
for i, s in enumerate(S):
    if s == 'o':
        maru.append(i)
    elif s == '?':
        hate.append(i)

if len(maru) > 4 or (len(maru) + len(hate) < 1):
    print(0)
elif len(maru) == 4:
    print(4 * 3 * 2 * 1)
elif len(maru) == 0:
    print(pow(len(hate), 4))
elif len(maru) == 1:
    print(pow(1 + len(hate), 4) - pow(len(hate), 4))
elif len(maru) == 2:
    print(
        pow(2 + len(hate), 4) - 2 * (pow(1 + len(hate), 4)) +
        pow(len(hate), 4))
else:
    print(
        pow(3 + len(hate), 4) - 3 * (pow(2 + len(hate), 4)) +
        3 * pow(1 + len(hate), 4) - pow(len(hate), 4))
