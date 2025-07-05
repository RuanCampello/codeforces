from collections import deque
# this code timeout and i didn't have the time to correct it so...

h, w, k = map(int, input().split())
goals = [tuple(map(int, input().split())) for _ in range(k)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

dp = [[-1] * (w + 2) for _ in range(h + 2)]
count = [[4] * (w + 2) for _ in range(h + 2)]

q = deque()

for r, c in goals:
    dp[r][c] = 0
    q.append((r, c))


def neighbors(i, j):
    res = []
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 1 <= ni <= h and 1 <= nj <= w:
            res.append((ni, nj))
        else:
            res.append(None)
    return res


neighbors_map = [[neighbors(i, j) for j in range(w + 2)] for i in range(h + 2)]

while q:
    i, j = q.popleft()
    for a in range(4):  # a = Aoki's choice direction
        for b in range(4):
            if b == a:
                continue
            di, dj = directions[b]
            ni, nj = i - di, j - dj
            if not (1 <= ni <= h and 1 <= nj <= w):
                continue

            if dp[ni][nj] != -1:
                continue

            count[ni][nj] -= 1

            if count[ni][nj] == 0:
                dp[ni][nj] = dp[i][j] + 1
                q.append((ni, nj))

total = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if dp[i][j] == -1:
            continue
        total += dp[i][j]

print(total)

