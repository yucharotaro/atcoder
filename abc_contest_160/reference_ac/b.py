X = int(input())
happy_500 = 0
happy_5 = 0

happy_500 = X // 500
X %= 500
happy_5 = X // 5
print((happy_500 * 1000) + (happy_5 * 5))
