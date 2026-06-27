# every window r*c xor should be 0
# (n-r+1)*(m-c+1) constraints out of n*m free bits, hence the count is 2^(bits)


def evaluate(n: int, m: int, r: int, c: int) -> int:
    row = m * (r - 1)
    col = n * (c - 1)
    overlap = (r - 1) * (c - 1)
    free_bits = row + col - overlap

    return pow(2, free_bits, MOD)


MOD = 998244353

total = int(input())
for _ in range(0, total):
    n, m, r, c = map(int, input().split())
    print(evaluate(n, m, r, c))
