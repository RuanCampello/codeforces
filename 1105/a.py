def evaluate(n: int, k: int):
    if k >= n:
        return n

    answer = k
    remainder = n - k
    cost = 2

    while remainder >= cost:
        t = min(k, remainder // cost)
        answer += t
        remainder -= cost * t

        if t < k:
            break
        cost *= 2

    return answer


total = int(input())
for _ in range(0, total):
    n, k = map(int, input().split())
    print(evaluate(n, k))
