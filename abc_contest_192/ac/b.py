S = input()
s_odd = S[::2]
s_even = S[1::2]

if s_odd and s_even:
    if s_odd.islower() and s_even.isupper():
        print("Yes")
    else:
        print("No")
else:
    if s_odd and s_odd.islower():
        print("Yes")
    else:
        print("No")

#if s_even and s_even.islower():
#    if s_odd and s_odd.isupper():
#        print("Yes")
#    elif len(s_odd) == 0:
#        print("Yes")
#elif s_odd and s_odd.islower():
#    if s_even and s_even.isupper():
#        print("Yes")
#    elif len(s_even) == 0:
#        print("Yes")
#else:
#    print("No")
