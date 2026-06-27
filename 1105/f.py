MOD = 998244353

total = int(input())
max_n = 1
q = []

for _ in range(total):
    n, m = map(int, input().split())
    q.append((n, m))
    max_n = max(max_n, n)

# factorials and inverse factorials mod p, up to the largest n we ll see
factorial = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    factorial[i] = factorial[i - 1] * i % MOD

inv_factorial = [1] * (max_n + 1)
inv_factorial[max_n] = pow(factorial[max_n], MOD - 2, MOD)
for i in range(max_n, 0, -1):
    inv_factorial[i - 1] = inv_factorial[i] * i % MOD

# close form derived from the tree-function GF
for n, m in q:
    common = factorial[n] * inv_factorial[m] % MOD  # n! / m! shared by each term
    answer = 0
    for j in range(m, n + 1):
        skeleton_pow = pow(j - 1, n - 1, MOD)  # (j-1)^(n-1), with 0^0 = 1
        if skeleton_pow == 0:  # j == 1 with n >= 2 contributes nothing :D
            continue

        bracket = (j - 1) * inv_factorial[n - j] % MOD
        if n - j - 1 >= 0:
            bracket = (bracket + inv_factorial[n - j - 1]) % MOD

        term = common * inv_factorial[j - m] % MOD * skeleton_pow % MOD * bracket % MOD

        if (n - j) & 1:
            answer -= term
        else:
            answer += term

    print(answer % MOD)

