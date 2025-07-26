from itertools import product

n, k, x = map(int, input().split())
strings = [input().strip() for _ in range(n)]

all_seq = product(range(n), repeat=k)
all_str = ["".join(strings[i] for i in seq) for seq in all_seq]
all_str.sort()

print(all_str[x - 1])
