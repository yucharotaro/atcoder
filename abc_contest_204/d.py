#def bin_search(y, T):
#    low = 0
#    high = len(T) + 1

#    while low <= high:
#        mid = (low + high) // 2
#        guess = T[mid]
#        if guess == y:
#            return mid
#        elif guess > y:
#            high = mid - 1
#        elif guess < y:
#            low = mid + 1

#    return None

N = int(input())
T = sorted(map(int, input().split()))

o1 = []
sum_o1 = 0
o2 = []
sum_o2 = 0
if len(T) < 2:
    print(T[0])
    exit()

flag = False
while len(T) != 0:
    t = 0
    if len(o1) == 0 or len(o2) == 0:
        t = T.pop()
    else:
        y = abs(sum(o1) - sum(o2))
        diff_y = 1000000000
        target_index = -1
        for i, t in enumerate(T):
            if diff_y > abs(y - t):
                target_index = i
                diff_y = abs(y - t)
            #print(diff_y, t, target_index)
        if flag:
            if y > T[target_index]:
                t = T.pop(target_index)
            else:
                t = T.pop()
        else:
            t = T.pop(target_index)

    if sum_o1 > sum_o2:
        o2.append(t)
        sum_o2 += t
        if sum_o2 > sum_o1:
            flag = True
    else:
        o1.append(t)
        sum_o1 += t
        if sum_o1 > sum_o2:
            flag = True

print(max(sum_o1, sum_o2))
