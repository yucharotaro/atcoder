s = input()
k = int(input())
cnt = 0

for e in s:
    if e == "1":
        cnt += 1
    else:
        print(e)
        exit()

    if cnt >= k:
        print(e)
        exit()
