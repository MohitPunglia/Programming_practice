# Count Vowels and Consonants => Given a string, count how many vowels (a, e, i, o, u) and consonants it contains, ignoring spaces, digits, and special characters. => Example: "Hello World" → 3 vowels, 7 consonants


def count_vowels(str):
    vowels = "aeiou"
    vowel_count = 0
    consonants_count = 0

    for ch in str:
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
                print(vowel_count)
            else:
                consonants_count += 1

    return vowel_count, consonants_count


print(count_vowels("Hello World"))
