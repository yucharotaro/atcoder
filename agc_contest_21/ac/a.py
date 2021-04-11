n = int(input())
ans = 0

list_n = list(map(int, str(n)))
min_keta = min(list_n)
min_keta_index = str(n).find(str(min_keta))

if min_keta_index == 0:
    tmp = str(list_n[0] - 1) + "9" * (len(list_n) - 1)
    ans = max(sum(list_n), sum(map(int, tmp)))
else:
    list_n[min_keta_index - 1] -= 1
    for i in range(min_keta_index, len(list_n)):
        list_n[i] = 9
    ans = sum(list_n)
print(ans)
