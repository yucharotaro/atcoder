X = input()
if X.count("."):
    print(X[:X.index(".")])
else:
    print(X)
