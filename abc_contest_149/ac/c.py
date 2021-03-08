def is_prime(n):
    if n <= 1:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


X = int(input())

while not is_prime(X):
    X += 1
print(X)
