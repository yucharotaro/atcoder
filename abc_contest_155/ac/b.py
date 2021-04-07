n = int(input())
A = list(map(int, input().split()))
even_A = [a for a in A if a % 2 == 0]

if len(even_A) > 0:
    for a in even_A:
        if a % 3 != 0 and a % 5 != 0:
            print("DENIED")
            exit()
    print("APPROVED")
else:
    print("APPROVED")
