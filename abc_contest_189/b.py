N, X = map(int, input().split())
v_list = [list(map(int, input().split())) for _ in range(N)]
ans = -1
sum_v = 0
for i, v_p in enumerate(v_list):
    sum_v += v_p[0] * v_p[1] / 100.0
    if (sum_v > X):
        ans = i + 1
        break
print(ans)
