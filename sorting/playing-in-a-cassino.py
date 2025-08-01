import sys

input = sys.stdin.read().split()

cursor = 0
t = int(input[cursor])
cursor += 1


for _ in range(t):
    n, m = map(int, input[cursor : cursor + 2])
    cursor += 2
    v = [[] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            temp = int(input[cursor])
            cursor += 1
            v[j].append(temp)

    res = 0
    for j in range(m):
        v[j].sort(reverse=True)
        for i in range(1, n + 1):
            res += v[j][i - 1] * (n - i)
            res -= v[j][i - 1] * (i - 1)
    print(res)
