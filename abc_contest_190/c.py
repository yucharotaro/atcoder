n, m = map(int, input().split())
ab_lists = [list(map(int, input().split())) for _ in range(m)]
flat_ab = [i for e in ab_lists for i in e]
k = int(input())
cd_lists = [list(map(int, input().split())) for _ in range(k)]
flat_cd = [i for e in cd_lists for i in e]

ans_set = set()
for cd_list in cd_lists:
    if (flat_cd.count(cd_list[0]) == 1):
        ans_set.add(cd_list[0])
    elif (flat_cd.count(cd_list[1]) == 1):
        ans_set.add(cd_list[1])
    else:
        if cd_list[0] not in ans_set:
            ans_set.add(cd_list[0])
        elif cd_list[1] not in ans_set:
            ans_set.add(cd_list[1])
        else:
            if (flat_ab.count(cd_list[0]) > flat_ab.count(cd_list[1])):
                ans_set.add(cd_list[0])
            else:
                ans_set.add(cd_list[1])

tsk = 0
for ab_list in ab_lists:
    ab_set = set(ab_list)
    if (ab_set.issubset(ans_set)):
        tsk += 1

print(tsk)
