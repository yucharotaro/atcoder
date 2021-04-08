n = int(input())
restraunts = []
for i in range(n):
    city, score = input().split()
    score = int(score)
    restraunts.append({"num": i + 1, "city": city, "score": score})

restraunts = sorted(restraunts, key=lambda r: (r["city"], -r["score"]))
for r in restraunts:
    print(r["num"])
