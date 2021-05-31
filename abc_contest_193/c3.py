N = int(input())

had = set()
for i in range(2, int(N**0.5) + 1):
    step = 2
    while i**step <= N:
        had.add(i**step)
        step += 1

print(N - len(had))
