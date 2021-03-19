dishes = [int(input()) for _ in range(5)]

now = sum(t for t in dishes if t % 10 == 0)
extra_dishes = [t for t in dishes if t % 10 != 0]
extra_dishes.sort(key=lambda t: t % 10, reverse=True)

len_extra_dishes = len(extra_dishes)
if len_extra_dishes > 0:
    for i in range(len_extra_dishes - 1):
        now += extra_dishes[i] + (10 - extra_dishes[i] % 10)
    now += extra_dishes[-1]
print(now)
