n, x = map(int, input().split())
a_list = list(map(int, input().split()))

ad_list = list(a for a in a_list if a != x)
if len(ad_list) == 0:
    print()
else:
    for a in a_list:
        if (a != x):
            print(a)
