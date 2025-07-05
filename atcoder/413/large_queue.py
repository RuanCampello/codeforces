from collections import deque

queries = int(input())

queue = deque()
cursor = 0
sum = 0

for _ in range(queries):
    p = input().split()

    if p[0] == "1":
        c, x = int(p[1]), int(p[2])

        queue.append((x, c))

    if p[0] == "2":
        k = int(p[1])
        c = 0

        while k > 0:
            x, cnt = queue[0]
            if cnt > k:
                c += x * k
                queue[0] = (x, cnt - k)
                k = 0

            else:
                c += x * cnt
                k -= cnt
                queue.popleft()
        print(c)
