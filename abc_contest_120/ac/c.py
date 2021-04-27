s = input()
zero = s.count("0")
one = len(s) - zero
print(2 * min(zero, one))
