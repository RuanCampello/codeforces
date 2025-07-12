from collections import deque

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for __ in range(N - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    distance = [-1] * (N + 1)
    q = deque([1])
    distance[1] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                q.append(v)

    res = [-1] * (N + 1)
    res[1] = 0
    q = deque([1])

    while q:
        u = q.popleft()
        visited = [False] * (N + 1)
        temp_q = deque([(u, 0)])
        visited[u] = True
        while temp_q:
            node, dist = temp_q.popleft()
            if dist == K:
                if res[node] == -1 or res[node] > res[u] + 1:
                    res[node] = res[u] + 1
                    q.append(node)
                continue
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    temp_q.append((neighbour, dist + 1))

    output = []
    for k in range(2, N + 1):
        output.append(str(res[k]))
    print(" ".join(output))

