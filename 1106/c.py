total = int(input())

for _ in range(0, total):
    n = int(input())
    parents = list(map(int, input().split()))

    depth = [0] * (n + 1)
    max_d = depth.copy()

    answer = n

    for i in range(2, n + 1):
        depth[i] = depth[parents[i - 2]] + 1

    for v in range(1, n + 1):
        max_d[v] = depth[v]

    # every child finalised before its parent reads it
    for i in range(n, 1, -1):
        parent = parents[i - 2]
        if max_d[i] > max_d[parent]:
            max_d[parent] = max_d[i]

    # two largest child max_d per v
    best_1 = [-1] * (n + 1)
    best_2 = best_1.copy()

    for i in range(2, n + 1):
        parent = parents[i - 2]
        v = max_d[i]
        if v > best_1[parent]:
            best_2[parent] = best_1[parent]
            best_1[parent] = v
        elif v > best_2[parent]:
            best_2[parent] = v

    for v in range(1, n + 1):
        if best_2[v] != -1:
            answer += best_2[v] - depth[v]
    print(answer)
