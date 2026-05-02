# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/python


def open_or_senior(data):
    categories = []

    for item in data:
        if item[0] >= 55 and item[1] > 7:
            categories.append("Senior")
        else:
            categories.append("Open")

    print(categories)
    return categories


open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])
