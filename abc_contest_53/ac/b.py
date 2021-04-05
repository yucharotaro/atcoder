s = input()
index_A = s.index("A")
index_Z = s[::-1].index("Z")
print(len(s[index_A:len(s) - index_Z]))
