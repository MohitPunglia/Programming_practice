# Check if a Number is Armstrong => An Armstrong number (also called a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the total number of digits.
# 153 -> 1^3 + 5^3 + 3^3 = 153
# 123 -> 1^3 + 2^3 + 3^3 = 36 != 123


def is_armstrong(number):
    num_str = str(number)
    power = len(num_str)
    total = 0

    for digit in num_str:
        total += int(digit) ** power

    print(total)
    print(number)

    return total == number


print(is_armstrong(1234))
