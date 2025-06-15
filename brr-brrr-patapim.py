quant = int(input())

for _ in range(quant):
    num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(num)]

    diagonal = dict()

    for line in range(num):
        for col in range(num):
            sum = line + col + 2  # because 0 index :)

            if sum not in diagonal:
                diagonal[sum] = set()
            diagonal[sum].add(matrix[line][col])

    p = [0] * (2 * num + 1)
    seen = set()
    for d in range(2, 2 * num + 1):
        value = list(diagonal[d])[0]
        p[d] = value
        seen.add(value)

    for x in range(1, 2 * num + 1):
        if x not in seen:
            p[1] = x
            break

    print(" ".join(str(p[idx]) for idx in range(1, 2 * num + 1)))
