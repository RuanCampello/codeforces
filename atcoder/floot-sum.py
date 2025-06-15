def floor_sum(n: int, m: int, a: int, b: int) -> int:
    res = 0
    while True:
        res += (n - 1) * n // 2 * (a // m)
        res += n * (b // m)
        a %= m
        b %= m

        y = (a * n + b) // m
        if y == 0:
            return res  # we wouldn't want a division by zero
        b = (a * n + b) % m
        n, a, m = y, m, a


t = int(input())
for _ in range(t):
    n, m, a, b = map(int, input().split())
    print(floor_sum(n, m, a, b))
