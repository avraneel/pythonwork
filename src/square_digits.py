def square_digits(num):
    ans = ""

    while num:
        d = num % 10
        sq = str(d * d)
        ans = sq + ans
        num = num // 10

    if ans == "":
        return 0

    return int(ans)


square_digits(9119)
square_digits(765)
