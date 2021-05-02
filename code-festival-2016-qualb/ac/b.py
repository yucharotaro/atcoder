n, a, b = map(int, input().split())
s = input()

passed = 0
b_passed = 0
for i in range(n):
    if s[i] == 'a' and passed < (a + b):
        passed += 1
        print("Yes")
        continue
    elif s[i] == 'b':
        if passed < (a + b) and b_passed < b:
            passed += 1
            b_passed += 1
            print("Yes")
            continue
        else:
            b_passed += 1
    print("No")
