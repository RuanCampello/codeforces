n, t = map(int, input().split())
k = list(map(int, input().split()))

left = 0
right = min(k) * t


def total_products(T):
    return sum(T // ki for ki in k)


res = right
while left <= right:
    mid = (left + right) // 2
    if total_products(mid) >= t:
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)
