N = input()
N_list = [int(n) for n in N]
k = len(N)
sum_n = sum(N_list)
a1 = a2 = 0

for n in N_list:
    if n % 3 == 1:
        a1 += 1
    elif n % 3 == 2:
        a2 += 1

sum_n_a = sum_n % 3
if sum_n_a == 0:
    print(0)
elif sum_n_a == 1:
    if a1 >= 1 and k > 1:
        print(1)
    elif a2 >= 2 and k > 2:
        print(2)
    else:
        print(-1)
elif sum_n_a == 2:
    if a2 >= 1 and k > 1:
        print(1)
    elif a1 >= 2 and k > 2:
        print(2)
    else:
        print(-1)
