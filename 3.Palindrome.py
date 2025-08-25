#  Check Palindrome (Number/String).  => Determine if the given string or integer reads the same forward and backward. Example: "madam" → Palindrome, 121 → Palindrome, 123 → Not Palindrome.


def check_palindrome(n):
    rev = ""

    for char in n:
        rev = char + rev

    if n == rev:
        print("Palindrome")

    return rev


print(check_palindrome("madm"))


def is_palindrome(n):
    return n == n[::-1]


print(is_palindrome("madam"))
