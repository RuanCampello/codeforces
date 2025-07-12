def count_valid_tuples_simple(N):
    MOD = 998244353
    ans = 0

    for b in range(1, N + 1):
        for c in range(1, b):
            q = 1
            while True:
                a = b * q + c
                if a > N:
                    break
                if a != b and a != c:
                    ans = (ans + 1) % MOD
                q += 1

    return ans % MOD


print(count_valid_tuples_simple(7))
print(count_valid_tuples_simple(441))
print(count_valid_tuples_simple(411111111114))

