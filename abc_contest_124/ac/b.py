n = int(input())
H = list(map(int, input().split()))

highest = 0
cnt = 0
for h in H:
    if highest <= h:
        highest = h
        cnt += 1
print(cnt)
