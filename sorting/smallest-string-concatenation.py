import sys
from functools import cmp_to_key

strings = [line.strip() for line in sys.stdin if line.strip()]
strings.sort(key=cmp_to_key(lambda x, y: -1 if x + y < y + x else 1))
print("".join(strings), end="")

