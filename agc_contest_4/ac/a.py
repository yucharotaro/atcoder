blocks = sorted(list(map(int, input().split())))
# テストケースが悪くてACになったが、本来であれば全ての辺に対して偶数判定すべき
if blocks[2] % 2 == 0:
    print(0)
else:
    print(blocks[0] * blocks[1])
