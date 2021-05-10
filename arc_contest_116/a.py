def sol(x):
    ans = ""
    odd = 0
    even = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

            if (x // i) % 2 == 0:
                even += 1
            else:
                odd += 1

    if odd > even:
        ans = "Odd"
    elif even > odd:
        ans = "Even"
    else:
        ans = "Same"

    return ans


T = int(input())
answers = []
for _ in range(T):
    N = int(input())
    answers.append(sol(N))

print("\n".join(answers))
