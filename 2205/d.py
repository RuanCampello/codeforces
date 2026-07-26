total = int(input())
output = []

MODULUS = 998244353


def arrange(size, cut, pivot):
    left_span = pivot - 1
    values = bytearray(size + 1)
    spares = [0] * (size + 1)

    curr_max = 0

    for i in range(left_span):
        v = cut[i]
        if v > curr_max:
            if values[v]:
                return 0

            values[v] = 1
            curr_max = v
        elif v == curr_max:
            spares[v] += 1
        else:
            return 0

    curr_max = 0
    for i in range(size - 2, left_span - 1, -1):
        v = cut[i]
        if v > curr_max:
            if values[v]:
                return 0
            values[v] = 1
            curr_max = v
        elif v == curr_max:
            spares[v] += 1
        else:
            return 0

    ways = 1
    smaller_unused = 0
    spares_placed = 0
    for v in range(1, size):
        for _ in range(spares[v]):
            room = smaller_unused - spares_placed
            if room <= 0:
                return 0
            ways = ways * room % MODULUS
            spares_placed += 1
        if not values[v]:
            smaller_unused += 1
    return ways


for _ in range(total):
    size = int(input())
    cut = list(map(int, input().split()))
    second = size - 1

    if max(cut) != second:
        output.append(0)
        continue

    # the peak block lies whole
    # on one side of n leaving n only two possible slots
    block_start = cut.index(second)
    block_end = size - 2 - cut[::-1].index(second)
    arrangements = 0

    for p in (block_start + 1, block_end + 2):
        arrangements += arrange(size, cut, p)
    output.append(arrangements % MODULUS)

print("\n".join(map(str, output)))
