import sys


def _solve(N, A, B):
    p = sum(a * b for a, b in zip(A, B))
    return p == 0


def solve(in_):
    N = int(next(in_))
    A = list(map(int, next(in_).split()))
    B = list(map(int, next(in_).split()))
    return _solve(N, A, B)

def main():
    answer = solve(sys.stdin.buffer)
    print('Yes' if answer else 'No')


if __name__ == '__main__':
    main()
