# Reverse a String => Given an input string, write a program to reverse the order of its characters => Example: "Java" → "avaJ".

# word = "Java"


def reverse_string(word):
    reverse = ""

    for char in word:
        reverse = char + reverse
    return reverse


print(reverse_string("kkolop"))
