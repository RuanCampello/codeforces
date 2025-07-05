from itertools import permutations

n = int(input())
s = [input().strip() for _ in range(n)]
count = 0
unique = set()

for a, b in permutations(s, 2):
    unique.add(a + b)

print(len(unique))
