# Python標準入力Tips

## TLE対策

読み込む行数が多い場合、以下の方法で入力処理を高速化できる。

```python:Python
from sys import stdin

input = stdin.readline
x = input().rstrip()
```

改行や空白文字を削除するためにrstrip()をつけておいた方が安全。

## 【1行】1文字

```python:Python
# 入力
abc
```

```python:Python
s = input()  # sはstr型
```

## 【1行】1数字

```python:Python
# 入力
10
```

```python:Python
n = int(input())  # nはint型
```

## 【1行】n文字

```python:Python
# 入力
abc
```

```python:Python
a,b,c = map(str, input())  # 1個の文字列の入力を受け取って、1文字ずつ変数に格納
```

```python:Python
# 入力
abc def ghi
```

```python:Python
a,b,c = input().split()  # 3個の文字列の入力を受け取る
```

入力される文字列がn個の場合はリストに格納した方が便利。

```python:Python
str_list = list(input().split())  # n個の文字列をリストに格納
```

## 【1行】n数字

```python:Python
# 入力
123
```

```python:Python
a,b,c = map(int, input())  # 1個の数字の入力を受け取って、1桁ずつ変数に格納
```

```python:Python
# 入力
1 2 3
```

```python:Python
a,b,c = map(int, input().split())  # 3個の数字の入力を受け取る
```

入力される数字がn個の場合はリストに格納した方が便利。

```python:Python
num_list = list(map(int, input().split()))  # n個の数字をリストに格納
```

## 【n行】1文字

最初にn回という入力回数が与えられ、その後に入力がある場合。

```python:Python
# 入力
3
aa
a
aaa
```

```python:Python
n = int(input())  # nは入力回数
str_list = [input() for _ in range(n)]
print(str_list)
```

```python:Python
# 出力
['aa', 'a', 'aaa']
```

## 【n行】1数字

```python:Python
# 入力
4
2
3
4
5
```

```python:Python
n = int(input())  # nは入力回数
num_list = [int(input()) for _ in range(n)]
print(num_list)
```

```python:Python
# 出力
[2, 3, 4, 5]
```

## 【n行】n文字

最初にn回という入力回数が与えられ、その後に入力がある場合。

```python:Python
# 入力
3
aaa b cc
d ee fff
gg hhh i
```

```python:Python
n = int(input())  # nは入力回数
str_list = []
for i in range(n):
    str_list.append(list(input().split()))
print(str_list)
```

```python:Python
# 出力
[['aaa', 'b', 'cc'], ['d', 'ee', 'fff'], ['gg', 'hhh', 'i']]
```

以下は内包表記を使った場合。

```python:Python
n = int(input())  # nは入力回数
str_list = [list(input().split()) for _ in range(n)]
```

## 【n行】n数字

```python:Python
# 入力
3
2 1 3
3 1 2 3
2 3 2
```

```python:Python
n = int(input())  # nは入力回数
num_list = []
for i in range(n):
    num_list.append(list(map(int,input().split())))
print(num_list)
```

```python:Python
# 出力
[[2, 1, 3], [3, 1, 2, 3], [2, 3, 2]]
```

内包表記を使った場合。

```python:Python
n = int(input())  # nは入力回数
num_list = [list(map(int, input().split())) for _ in range(n)]
```

n行の入力をワンライナーで全て変数に代入したい場合。

```python:Python
a, b, c, d = map(int, open(0).read().split())
```

n行n数字の入力を個別に変数に代入したい場合。

```python:Python
n = int(input())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
for i in range(n):
    a[i], b[i] = map(int, input().split())
```

## 特定の文字列まで読み込み続ける

```python:Python
# 入力
1
1
2
3
5
-1
```

```python:Python
# 「-1」の文字列まで読み込みを続ける
for e in iter(input, '-1'):
    pass
```

## 行列の転置

リスト、タプルは*で展開できる。これを利用して行列の転置を簡潔にできる。

```python:Python
# 入力
list_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

```python:Python
print(list(map(list, zip(*list_matrix))))
```

```python:Python
# 出力
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

```python:Python
print(list(zip(*list_matrix)))
```

```python:Python
# 出力
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

## 数値を各桁ごとに扱う

```python:Python
n = int(input())

# 各桁の総和
print(sum(map(int, str(n))))
```

または以下。

```python:Python
n = int(input())

# 各桁の総和
ans = 0
while n > 0:
    ans += n % 10
    n //= 10
print(ans)
```
