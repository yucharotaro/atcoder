a, b = map(int, input().split())

ans = (a + b) / 2
print(int(ans) if ans.is_integer() else "IMPOSSIBLE")
