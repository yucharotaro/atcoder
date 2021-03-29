n = int(input())

words = []
for _ in range(n):
    words.append(input())

if len(set(words)) == n:
    for i in range(1, n):
        if words[i][0] != words[i - 1][-1]:
            print("No")
            exit()
else:
    print("No")
    exit()

print("Yes")
