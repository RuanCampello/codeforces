def minimum_signal_strength(n, m, houses):
    houses.sort()

    def can_cover(limit):
        i = 0
        count = 0
        while i < n:
            count += 1
            j = i
            while j < n and houses[j] - houses[i] <= 2 * limit:
                j += 1
            x = (houses[i] + houses[j - 1]) / 2
            reach = 2 * limit
            i = j
            while i < n and abs(houses[i] - x) <= reach:
                i += 1
        return count <= m

    lo, hi = 0, max(houses) - min(houses)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_cover(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo * m


n, m = map(int, input().split())
houses = list(map(int, input().split()))

print(minimum_signal_strength(n, m, houses))
