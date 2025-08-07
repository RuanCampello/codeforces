n = int(input())

arr = list(map(int, input().split()))
q = int(input())

arr.sort()


def binary_search(arr: list[int], needle: int):
    left, right = 0, len(arr)
    while left < right:
        middle = (left + right) // 2

        if arr[middle] > needle:
            right = middle
        else:
            left = middle + 1

    return left


for _ in range(q):
    m = int(input())
    count = binary_search(arr, m)
    print(count)
