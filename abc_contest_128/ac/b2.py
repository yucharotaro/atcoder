N = int(input())
restraunts = []
for i in range(N):
    city, score = input().split()
    restraunts.append([i + 1, city, int(score)])

restraunts.sort(key=lambda x: (x[1], -x[2]))
for i, _, _ in restraunts:
    print(i)
