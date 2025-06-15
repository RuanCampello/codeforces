quant = int(input())

for _ in range(quant):
    string = str(input())
    first_letters = [word[0] for word in string.strip().split(" ")]
    print("".join(first_letters))
