t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    res = []
    stack = [(0, n)]  # (start, b) where segment is 2^b
    while stack:
        start, b = stack.pop()
        if b == 0:
            res.append(p[start])
            continue
        segment_size = 1 << b
        half_size = 1 << (b - 1)
        left_start = start
        right_start = start + half_size

        left_min = min(p[left_start : left_start + half_size])
        right_min = min(p[right_start : right_start + half_size])

        if left_min > right_min:
            # reverse the segment of 2^b
            p[start : start + segment_size] = p[start : start + segment_size][::-1]

        # left and right halves
        stack.append((right_start, b - 1))
        stack.append((left_start, b - 1))

    print(" ".join(map(str, res)))
