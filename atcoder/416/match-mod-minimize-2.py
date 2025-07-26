from bisect import bisect_left
from sortedcontainers import SortedList
import sys

input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

answers = []
for _ in range(t):
    n = int(data[index])
    m = int(data[index + 1])
    index += 2

    A = list(map(int, data[index : index + n]))
    index += n
    B = list(map(int, data[index : index + n]))
    index += n

    A.sort()
    sl = SortedList(A)
    total = 0

    for b in B:
        target = (m - b) % m
        pos = sl.bisect_left(target)

        if pos < len(sl):
            a = sl[pos]
        else:
            a = sl[0]

        total += (a + b) % m
        sl.remove(a)
    answers.append(str(total))

print("\n".join(answers))
