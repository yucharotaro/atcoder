n, m = map(int, input().split())
foods = set(i for i in range(1, m + 1))
for _ in range(n):
    k, *A = map(int, input().split())
    foods = foods & set(A)
print(len(foods))
