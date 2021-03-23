S = input()
t = S[0::2].count('0') + S[1::2].count('1')
print(min(t, len(S) - t))
