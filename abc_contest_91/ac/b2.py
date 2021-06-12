card = dict()
N = int(input())
for _ in range(N):
    s = input()
    if s in card:
        card[s] += 1
    else:
        card[s] = 1
M = int(input())
for _ in range(M):
    t = input()
    if t in card:
        card[t] -= 1

ans = max(card.values())
if ans < 0:
    print(0)
else:
    print(ans)
