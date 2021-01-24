S = input()

print("YES" if len(
    S.replace("eraser", "").replace("erase", "").replace("dreamer", "").
    replace("dream", "")) == 0 else "NO")
