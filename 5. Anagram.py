def check_an(str1, str2):
    char_count = {}

    for ch in str1:
        char_count[ch] = char_count.get(ch, 0) + 1

        print(ch)

    for ch in str2:
        if ch not in char_count:
            return False

        char_count[ch] = char_count[ch] - 1

        if char_count[ch] < 0:
            return False

    return True


# print(check_an("listen", "silentt"))


def check_an1(str1, str2):
    for i in str1:
        for j in str2:
            if i == j:
                print(i)
        print("####" + j)


print(check_an("listen", "silentt"))
