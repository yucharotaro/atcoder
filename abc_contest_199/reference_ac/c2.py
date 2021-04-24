N = int(input())
S = list(input())

change = 0

Q = int(input())
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 2:
        change ^= 1
    else:
        A -= 1
        B -= 1
        if change == 0:
            S[A], S[B] = S[B], S[A]
        else:
            if A >= N:
                A -= N
            else:
                A += N
            if B >= N:
                B -= N
            else:
                B += N
            S[A], S[B] = S[B], S[A]
    #print(f"change = {change}, A = {A}, B = {B}, S = {S}")

if change:
    S = S[N:] + S[:N]

print(''.join(S))
