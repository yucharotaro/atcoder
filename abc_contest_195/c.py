N = int(input())
sep = 10**3
ans = 0
comma = 0

if N < 10**3:
    print(0)
    exit()
if N >= 10**3 and N < 10**6:
    ans += N % (10**3) + 1
if N >= 10**6 and N < 10**9:
    ans += 2 * (N % (10**9)) + 1
if N >= 10**9 and N < 10**12:
    ans += 3 * (N % (10**9)) + 1
if N >= 10**12 and N < 10**15:
    ans += 4 * (N % (10**12)) + 1
if N >= 10**15:
    ans += 5 * (N % (10**15)) + 1

print(ans)

#while True:
#    if tmp // sep > 0:
#        ans += comma * (tmp % sep) + 1
#        tmp -= sep
#    else:
#        ans = comma * (tmp % sep) + 1
#        break
#    comma += 1
#    sep *= 10**3
#print(ans if ans == 0 else ans - 1)

#if tmp <= sep - 1:
#    print(0)
#    exit()
#else:
#    tmp -= sep - 1
#    sep *= 10**3

#cnt = 0
#comma = 1
#while True:
#    print(cnt, comma, sep - 1, tmp)
#    if tmp >= sep - 1:
#        print(tmp - (sep - 1))
#        cnt += comma * (sep - 1)
#        # tmp -= sep - 1
#    else:
#        cnt += comma * ((sep - 1) - tmp)
#        break
#    comma += 1
#    sep *= 10**3
#print(cnt)

#print(f"tmp = {tmp}, cnt = {cnt}, sep = {sep}")
#while True:
#    if tmp > sep - 1:
#        print(f"tmp = {tmp}, cnt = {cnt}, sep = {sep}, comma = {comma}")
#        cnt += tmp - (sep - 1) * comma
#        tmp -= sep - 1
#        sep *= 10**3
#        comma += 1
#    else:
#        cnt += tmp * comma
#        break
#print(cnt)
