K = int(input())

even = [i for i in range(1, K + 1) if i % 2 == 0]
odd = [i for i in range(1, K + 1) if i % 2 != 0]
print(len(even) * len(odd))
