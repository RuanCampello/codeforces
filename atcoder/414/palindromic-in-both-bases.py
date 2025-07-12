def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def in_base(n: int, b: int) -> str:
    res = ""

    while n > 0:
        res = str(n % b) + res
        n //= b
    return res or "0"


def generate_decimal_palindromes(limit: int):
    i = 1
    while True:
        s = str(i)
        # odd length
        odd = int(s + s[-2::-1])
        if odd > limit:
            break
        yield odd
        # even length
        even = int(s + s[::-1])
        if even <= limit:
            yield even
        i += 1


a = int(input())
n = int(input())
res = 0

for x in generate_decimal_palindromes(n):
    if is_palindrome(in_base(x, a)):
        res += x
print(res)
