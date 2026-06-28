# TLE on test 3  FUCK
#
# total = int(input())
#
# for _ in range(0, total):
#    n = int(input())
#    cakes = str(input())
#
#    states = {(0, 0): 0}
#
#    for cake in cakes:
#        if cake == "F":
#            steps = (1,)
#        elif cake == "T":
#            steps = (-1,)
#        else:
#            steps = (1, -1)  # worst for chell
#
#        nxt = {}
#
#        for (run, worst), fakes in states.items():
#            for step in steps:
#                new = run + step
#                if new < 0:
#                    new = 0
#
#                new_worst = worst if worst > new else new
#                value = fakes + (1 if step == 1 else 0)
#                key = (new, new_worst)
#
#                if value > nxt.get(key, -1):
#                    nxt[key] = value
#        states = nxt
#    print(max(fakes - worst for (_, worst), fakes in states.items()))
#

total = int(input())
for _ in range(0, total):
    n = int(input())
    cakes = input()
    max_fakes = sum(1 for c in cakes if c != "T")
    answer = -1

    for cap in range(n + 1):
        reach = [-1] * (cap + 1)
        reach[0] = 0
        for c in cakes:
            nxt = [-1] * (cap + 1)
            for h in range(cap + 1):
                v = reach[h]
                if v == -1:
                    continue
                if c != "T":  # fake = +1, allowed for F and N
                    up = h + 1
                    if up <= cap and v + 1 > nxt[up]:
                        nxt[up] = v + 1
                if c != "F":  # real = -1, allowed for T and N
                    down = h - 1 if h else 0
                    if v > nxt[down]:
                        nxt[down] = v
            reach = nxt

        best = max(reach)
        if best != -1 and best - cap > answer:
            answer = best - cap
        if best == max_fakes:
            break

    print(answer)
