# Find Missing Numbers from 1 to N => Given an unsorted array containing distinct integers from 1 to N (with some numbers missing), return all missing numbers => Example: arr = {1, 3, 5, 6} → Output: 2, 4


def find_missing_no(arr, no):
    missing = []

    for num in range(1, no + 1):
        if num not in arr:
            missing.append(num)

    return missing


print(find_missing_no(arr=[1, 3, 5, 6], no=6))
