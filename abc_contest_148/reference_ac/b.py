_ = input()
S, T = input().strip().split(' ')
print(''.join(s + t for s, t in zip(S, T)))
