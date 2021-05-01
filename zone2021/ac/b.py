N, D, H = map(int, input().split())
towers = [list(map(int, input().split())) for _ in range(N)]

ans_hights = []
for tower in towers:
    t_h = tower[1]
    t_d = tower[0]
    ans_hights.append(max(0, H - ((H - t_h) * (D / (D - t_d)))))
print(max(ans_hights))
