
"""

1 - делим массив на две части
2 - на какой части лежит искомое значение ?
3 - сокращаем интервал

"""

print(3//2)
# [1,2,3,4,5,6] 30
def search_in_sorted_list(values: list, value: int) -> bool:
    i = 0
    j = (len(values ) -1)

    while i<= j:
        m = (i + j) // 2

        if values[m] > value:
            j = m - 1
        elif values[m] < value:
            i = m + 1
        else:
            return True

    return False


# 1 2 3 4 5 6

# -5 -3 4. 6 10

# -5 -3  1 2 4 4

# 1 2 3 4 [5 6 7 8 9 10] -> 8
i = 4
j = 9

assert search_in_sorted_list([1, 2, 3, 5, 6], 5)
assert not search_in_sorted_list([1, 2, 3, 5, 6], -1)
assert not search_in_sorted_list([], 10)
assert search_in_sorted_list([1], 1)