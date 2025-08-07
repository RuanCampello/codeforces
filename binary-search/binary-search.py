n, q = map(int, input().split())
arr = list(map(int, input().split()))


def binary_search(arr: list[int], needle: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == needle:
            return middle + 1
        elif arr[middle] < needle:
            left = middle + 1
        else:
            right = middle - 1

    return -1


for _ in range(q):
    needle = int(input())
    print(binary_search(arr, needle))
