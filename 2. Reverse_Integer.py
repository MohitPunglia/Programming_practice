# Reverse an Integer => Given an integer, reverse its digits without converting it to a string (optional challenge) => Example: 1234 → 4321 and -456 → -654.


def rev_int(number):
    negative_num = number < 0
    number = abs(number)

    rev_num = 0

    while number > 0:
        rem = number % 10
        rev_num = rev_num * 10 + rem
        number = number // 10

    if negative_num:
        rev_num = -rev_num

    return rev_num


print(rev_int(-632))
