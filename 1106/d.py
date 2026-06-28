total = int(input())

MAX = 10**6
smallest_poss_factor = list(range(MAX + 1))

i = 2

while i * i <= MAX:
    if smallest_poss_factor[i] == i:  # i is prime(?)
        for j in range(i * i, MAX + 1, i):
            if smallest_poss_factor[j] == j:  # keep the smallest
                smallest_poss_factor[j] = i
    i += 1

for _ in range(0, total):
    n = int(input())

    distinct = 0
    prime_counted = 0

    while n > 1:
        p = smallest_poss_factor[n]
        distinct += 1

        while n % p == 0:
            n //= p
            prime_counted += 1
    print(distinct + prime_counted - 1)
