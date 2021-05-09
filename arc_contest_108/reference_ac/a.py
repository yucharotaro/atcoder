S, P = map(int, input().split())
for i in range(1000050):
    if i * (S - i) == P:
        print("Yes")
        exit(0)
print("No")
