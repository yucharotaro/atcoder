from itertools import combinations

antenna = [int(input()) for _ in range(5)]
k = int(input())

for one, two in combinations(antenna, 2):
    if abs(one - two) > k:
        print(":(")
        exit()
print("Yay!")
