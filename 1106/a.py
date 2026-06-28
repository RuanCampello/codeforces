total = int(input())
for _ in range(0, total):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    total = sum(a) - sum(b)

    if all(a_i >= b_i for a_i, b_i in zip(a, b)):
        print(total)
    elif all(x >= y for x, y in zip(sorted(a), sorted(b))):
        print(total + c)
    else:
        print(-1)
