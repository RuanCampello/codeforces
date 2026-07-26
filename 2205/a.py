total = int(input())

for _ in range(total):
    n = int(input())
    w = list(map(int, input().split()))

    if n % 2:
        print("NO")
    else:
        print("YES" if min(w[0::2]) - max(w[1::2]) >= 2 else "NO")
