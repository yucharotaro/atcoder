n = input()
n_list = list(e for e in map(int, n))
print("Yes" if sum(n_list) % 9 == 0 else "No")
