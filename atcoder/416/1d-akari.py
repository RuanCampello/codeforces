s = str(input())
t = list(s)
i = 0
while i < len(s):
    if s[i] == ".":
        j = i

        while j < len(s) and s[j] == ".":
            j += 1
        mid = (i + j - 1) // 2

        for k in range(i, j):
            t[k] = "."
        t[mid] = "o"

        i = j
    else:
        t[i] = "#"
        i += 1

print("".join(t))
