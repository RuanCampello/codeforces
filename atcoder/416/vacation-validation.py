n, l, r = map(int, input().split())
s = str(input())

print("Yes") if all(c == "o" for c in s[l - 1 : r]) else print("No")
