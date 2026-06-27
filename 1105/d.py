total = int(input())

for _ in range(total):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    coeficient_of_happiness = (2 * d) + 1  # itself and the two d in around
    window = sum(a[-d:]) + sum(a[: d + 1])  # window centered on person 0

    answer = 0

    for i in range(n):
        # the value of givin the gift to person i
        happinness = coeficient_of_happiness * a[i] - window
        if happinness > 0:
            answer += happinness

        window += a[(i + d + 1) % n] - a[(i - d) % n]  # slide center from i to i + 1
    print(answer)
