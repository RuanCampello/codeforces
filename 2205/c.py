total = int(input())
output = []

for _ in range(total):
    n = int(input())
    el = [tuple(map(int, input().split())) for _ in range(n)]
    b = 0

    for m in range(n, 0, -1):
        current = 0

        for l, r, u, v in el:
            # p is the slot of this element would land in
            # q is the right rank for this m
            p = current + 1
            q = m + 1 - p

            if (p < l or p > r) and (q < u or q > v):
                current += 1
                if current == m:
                    break
        if current == m:
            b = m
            break

    output.append(b)
print("\n".join(map(str, output)))
