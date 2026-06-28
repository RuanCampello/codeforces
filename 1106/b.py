total = int(input())
for _ in range(0, total):
    n = int(input())
    answer = 0

    for b in range(1, n + 1):
        # the condition reduces to b | a and b | c :X
        q = n // b  # multiples of b in [1, n] valid for both
        # so q is a or b choseen independently
        answer += q * q
    print(answer)
