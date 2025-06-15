quant = int(input())
for _ in range(quant):
    n, m, left, right = map(int, input().split())
    a = -left
    b = right
    x = min(a, m // 2 + m % 2)  # prefer the left expansion
    y = m - x
    if y > b:
        y = b
        x = m - y
    print(-x, y)
