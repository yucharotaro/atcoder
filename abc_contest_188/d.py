from sys import stdin

if __name__ == "__main__":
    n,c = map(int, input().split())
    list_a = list_b = list_c = []
    for _ in range(n):
        a,b,c = [map(int, input().split())]
        list_a.append(a)
        list_b.append(b)
        list_c.append(c)

