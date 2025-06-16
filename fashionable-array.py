t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # already fashionable
    if (min(a) + max(a)) % 2 == 0:
        print(0)
        continue

    unique = list(set(a))
    best = 0
    for lo in unique:
        for hi in unique:
            if (lo + hi) % 2 == 0:
                count = sum(lo <= x <= hi for x in a)
                best = max(best, count)

    print(n - best)

