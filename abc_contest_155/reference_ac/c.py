import sys
from collections import Counter
N = int(sys.stdin.readline())
S = sys.stdin.read().split()

count = Counter(S)
max_num = max(count.values())

max_list = []

for i, j in count.items():
    if j == max_num:
        max_list.append(i)

max_list.sort()

print('\n'.join(max_list))
