# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python


def descending_order(num):
    digits = []

    while num:
        d = num % 10
        digits.append(d)
        num = num // 10

    digits.sort(reverse=True)

    # build new number
    ans = 0

    for digit in digits:
        ans = (ans * 10) + digit

    print(ans)
    return ans


descending_order(42145)
