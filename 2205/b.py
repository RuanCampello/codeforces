total = int(input())

output = []

for _ in range(total):
    n, k = map(int, input().split())

    if k == n - 1:
        output.append("-1")
        continue

    m = n - k
    extra = (n + 1) // 2 - (m + 1) // 2
    extra_1s = n // 2 - m // 2
    blocks = ["0" * (1 + extra), "1" * (1 + extra_1s)]

    for i in range(2, m):
        blocks.append("01"[i % 2])
    output.append("".join(blocks))

print("\n".join(output))
