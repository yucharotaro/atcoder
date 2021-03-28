def solve(s, i, bind, ans):
    #print(i, bind, ans)
    if i == len(s):
        return ans + int(bind)
    return solve(s, i + 1, s[i],
                 int(bind) + ans) + solve(s, i + 1, bind + s[i], ans)


s = list(input())
print(solve(s, 1, s[0], 0))
