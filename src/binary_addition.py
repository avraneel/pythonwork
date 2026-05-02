# https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python


def add_binary(a, b):
    c = bin(a + b)

    print(int(c[2:]))
    return c[2:]


add_binary(5, 9)
