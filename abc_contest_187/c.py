n = int(input())
s_list = [input() for _ in range(n)]

for t in s_list:
    if (t[:1] == "!" and t[1:] in s_list):
        print(t)
        exit()
    elif (t[:1] != "!" and "!" + t in s_list):
        print(t)
        exit()

print("satisfiable")
