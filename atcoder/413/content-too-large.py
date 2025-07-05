_, m = map(int, input().split())
a = list(map(int, input().split()))
total = sum(a)

if total > m:
    print("No")
else:
    print("Yes")
