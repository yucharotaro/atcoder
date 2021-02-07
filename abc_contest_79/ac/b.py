N = int(input())
li = [2, 1]
for i in range(2, N + 1):
    li.append(li[i - 1] + li[i - 2])
print(li.pop())
