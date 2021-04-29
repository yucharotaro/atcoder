a, b, c = map(int, input().split())
cnt = 0

if a == b == c:
    print(cnt)
    exit()

max_n = max(a, b, c)
step = float("INF")
step_cnt = 0
for e in (a, b, c):
    if e != max_n:
        step = min(step, max_n - e)
        step_cnt += 1
if step_cnt >= 2:
    cnt += step
    if a != max_n:
        a += step
    if b != max_n:
        b += step
    if c != max_n:
        c += step

for e in (a, b, c):
    if e != max_n:
        if (max_n - e) % 2 == 0:
            cnt += (max_n - e) // 2
        else:
            cnt += (max_n - e) // 2 + 2

print(cnt)
