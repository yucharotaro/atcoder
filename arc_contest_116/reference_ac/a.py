import sys
input = sys.stdin.readline
write = sys.stdout.write

T = int(input())
X = [""] * T
for i in range(T):
    N = int(input())

    if N % 2:
        X[i] = "Odd"
    elif N % 4:
        X[i] = "Same"
    else:
        X[i] = "Even"

write("\n".join(X))
