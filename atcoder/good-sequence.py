from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

freq = Counter(arr)
removals = 0

for n, count in freq.items():
    if count < n:
        removals += count
    else:
        removals += count - n

print(removals)
