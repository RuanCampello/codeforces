def run_lengths(st):
    runs = []
    for ch in st:
        if not runs or runs[-1][0] != ch:
            runs.append([ch, 1])
        else:
            runs[-1][1] += 1
    return runs


quant = int(input())
for _ in range(quant):
    p = input().strip()
    s = input().strip()

    rp = run_lengths(p)
    rs = run_lengths(s)

    if len(rp) != len(rs) or any(rp[i][0] != rs[i][0] for i in range(len(rp))):
        print("NO")
        continue

    ok = True
    for (c, a), (_, b) in zip(rp, rs):
        if not (a <= b <= 2 * a):
            ok = False
            break

    print("YES" if ok else "NO")
