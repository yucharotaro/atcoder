a, b, c = map(int, input().split())
if a == b == c and a % 2 == 0:
    print(-1)
    exit()
count = 0
while not (a % 2 or b % 2 or c % 2):
    count += 1
    a, b, c = b // 2 + c // 2, a // 2 + c // 2, a // 2 + b // 2
print(count)
