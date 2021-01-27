maxN, M, T = map(int, input().split())
in_out_times = [list(map(int, input().split())) for _ in range(M)]
N = maxN

now = 0
for in_out_time in in_out_times:
    in_time, out_time = in_out_time
    use_time = in_time - now
    cafe_time = out_time - in_time
    N -= use_time
    if (N <= 0):
        print("No")
        exit()
    N += cafe_time
    if (N > maxN):
        N = maxN
    now = out_time

use_time = T - now
print("Yes" if N - use_time > 0 else "No")
