import math

N = int(input())
A = list(range(2, N + 1))
p = [1]
y = []
while A[0]**2 <= N:
    tmp = A[0]
    p.append(tmp)
    # 約数があるもの
    Y = [e for e in A if e % tmp == 0]
    y_tmp = []
    for i in range(1, len(Y)):
        # a^b(a,b >= 2)で表せないもの
        if not math.log(Y[i], Y[0]).is_integer():
            y.append(Y[i])
        else:
            # a^b(a,b >= 2)で表せるもの
            y_tmp.append(Y[i])
    y = list(set(y) - set(y_tmp))
    A = [e for e in A if e % tmp != 0]
# N以下の素数
enes = p + A
print(N - len(enes) - len(y))
