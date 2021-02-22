N = int(input())
a = sorted(list(map(int, input().split())))[::-1]

alice = a[::2]
bob = a[1::2]
print(sum(alice) - sum(bob))
