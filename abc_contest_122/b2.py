import re
S = input()
split_S = re.split("[^ACGT]", S)
print(len(max(split_S)))
