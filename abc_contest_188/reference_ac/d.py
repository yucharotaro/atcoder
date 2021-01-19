import sys
from itertools import islice
from collections import defaultdict


def _solve(N, C, query):
    ans = 0
    cost = 0

    day0 = 0
    for day1 in sorted(query):
        ans += (day1 - day0) * min(cost, C)
        diff = query[day1]
        cost += diff
        day0 = day1

    return ans


def solve(in_):
    N, C = map(int, next(in_).split())
    query = defaultdict(int)
    for line in islice(in_, N):
        a, b, c = map(int, line.split())
        query[a] += c
        query[b + 1] -= c
    return _solve(N, C, query)


def main():
    answer = solve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
