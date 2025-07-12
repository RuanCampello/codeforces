n = int(input())

string = str()
is_great = False
for _ in range(n):
    le, c = input().split()
    c = int(c)
    if c // n <= 100:
        string += le * c
    else:
        is_great = True

if len(string) > 100 or is_great:
    print("Too Long")
else:
    print(string)
