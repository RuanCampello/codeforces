from fractions import Fraction
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # trivial case
    if n <= 2:
        print("Yes")
        continue

    cnt = Counter(a)
    mags = sorted(abs(x) for x in a)
    # forward
    r_abs = Fraction(mags[1], mags[0])
    ok = True
    for i in range(2, n):
        if Fraction(mags[i], mags[i - 1]) != r_abs:
            ok = False
            break
    if not ok:
        print("No")
        continue

    found = False
    # backward
    for r_sign in (r_abs, -r_abs):
        sign_of_r = 1 if r_sign > 0 else -1
        for start_sign in (1, -1):
            seq = []
            cur_sign = start_sign
            for m in mags:
                seq.append(cur_sign * m)
                cur_sign *= sign_of_r
            if Counter(seq) == cnt:
                print("Yes")
                found = True
                break
        if found:
            break

    if not found:
        print("No")
