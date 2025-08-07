n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

left = 0
right = min(b[i] // a[i] for i in range(n)) + k


def is_possible(x):
    needed = 0
    for i in range(n):
        needed += max(0, a[i] * x - b[i])
        if needed > k:
            return False
    return needed <= k


res = 0
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
