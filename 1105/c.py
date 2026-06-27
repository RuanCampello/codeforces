MOD = 998244353

total = int(input())

for _ in range(total):
    n = int(input())
    a = list(map(int, input().split()))

    positives = sum(1 for x in a if x > 0)
    if positives <= 1:  # alice cant do a move
        print(0)
        continue

    xor = 0
    for value in a:
        xor ^= value
    if xor == 0:  # only winning move is b == a
        print(1)
    else:
        tbit = xor.bit_length() - 1
        print(sum((value >> tbit) & 1 for value in a) % MOD)

