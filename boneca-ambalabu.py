quant = int(input())

for _ in range(quant):
    num = int(input())
    arr = list(map(int, input().split()))

    max_sum = 0
    for x in arr:
        current_sum = sum(x ^ y for y in arr)
        max_sum = max(max_sum, current_sum)
    print(max_sum)
