a, b, c = map(int, input().split())

while True:
    if c == 0:
        a -= 1
        if (a < 0):
            print("Aoki")
            exit()
        b -= 1
        if (b < 0):
            print("Takahashi")
            exit()
    else:
        b -= 1
        if (b < 0):
            print("Takahashi")
            exit()
        a -= 1
        if (a < 0):
            print("Aoki")
            exit()
