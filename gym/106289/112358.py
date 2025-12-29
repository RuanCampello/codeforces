MOD = 998244353

# Rules:
#
# There are a total of 16 squares, and each move can shift the tiles up, down, left, or right.
# If two adjacent numbers satisfy the condition that they are consecutive terms in the Fibonacci sequence,
# they will merge into their sum, and the score increases by the value of the new number.
#
# After each move, you can either add a new number 1,
# or not add at all. Note that the newly added 1 is not included in the total score.


board: list[list[int]] = [list(map(int, input().split())) for _ in range(4)]
max_n = max(max(row) for row in board)

fib = [0] * (max_n + 1)
if max_n >= 1:
    fib[1] = 1
if max_n >= 2:
    fib[2] = 1

for i in range(3, max_n + 1):
    fib[i] = (fib[i - 1] + fib[i - 2]) % MOD

score_fib = [0] * (max_n + 1)

for i in range(3, max_n + 1):
    score_fib[i] = (fib[i] + score_fib[i - 1] + score_fib[i - 2]) % MOD

total = 0
for row in board:
    for cell in row:
        if cell >= 3:
            total = (total + score_fib[cell]) % MOD

print(total)
