def c_time3_or_div2(N, A):
    # Aの各要素aにおける因数2の個数の和
    # aを2進数として下位ビットから見て、最初に1が現れた桁数が因数2の個数
    print([bin(a)[::-1].index('1') for a in A])
    return sum((bin(a)[::-1].index('1') for a in A))


N = int(input())
A = [int(i) for i in input().split()]
print(c_time3_or_div2(N, A))
