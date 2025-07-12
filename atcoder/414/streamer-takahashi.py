n, fr, to = map(int, input().split())

watchers = 0
for _ in range(n):
    x, y = map(int, input().split())

    if x <= fr and y >= to:
        watchers += 1
print(watchers)
