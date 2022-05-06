from collections import Counter


def missingNumbers(arr, brr):
    # Write your code here
    a = Counter(arr)
    b = Counter(brr)
    return sorted((b - a).keys())


arr = [11, 4, 11, 7, 13, 4, 12, 11, 10, 14]
brr = [11, 4, 11, 7, 3,7, 10, 13, 4, 8, 12, 11, 10, 14, 12]

print(missingNumbers(arr, brr))