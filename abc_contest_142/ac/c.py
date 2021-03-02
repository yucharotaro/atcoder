N = int(input())
A = list(map(int, input().split()))
indexes = list(range(len(A)))
sorted_indexes = [str(i + 1) for i in sorted(indexes, key=lambda i: A[i])]
print(" ".join(sorted_indexes))
