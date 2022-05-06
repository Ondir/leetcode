# 3. Get n largest or n smallest elements in a list using the module heapq
import heapq

scores = [51, 33, 64, 87, 91, 75, 15, 49, 33, 82]

print(heapq.nlargest(1, scores))
print(heapq.nsmallest(1, scores))

print(*scores)
# 5. Get all the elements in the middle of the list
_, *mid, _ = [51, 33, 64, 87, 91, 75, 15, 49, 33, 82]
print(mid)
# 6 Assign multiple variables in just one line
one, two, three, four = 1, 2, 3, 4
# 9. Repeat strings without looping

s = 'asd'
print(s * 5)
# 10. Compare 3 numbers just like in Math

x = 4
print(1 < x < 10)

# 11. Merge dictionaries in a single readable line

first_dictionary = {'name': 'Fatos', 'location': 'Munich'}
second_dictionary = {'name': 'Fatos', 'surname': 'Morina',
                     'location': 'Bavaria, Munich'}
result = first_dictionary | second_dictionary
print(result)

# 12. Find the index of an element in a tuple

books = ('Atomic habits', 'Ego is the enemy', 'Outliers', 'Mastery')
print(books.index('Mastery'))

# 13. Convert a string into a list of strings

import ast


def string_to_list(string):
    return ast.literal_eval(string)


string = "[[1, 2, 3],[4, 5, 6]]"
my_list = string_to_list(string)
print(my_list)

# 23. Reverse the ordering of a list
my_list = ['a', 'b', 'c', 'd']

print(my_list[::-1])
my_list.reverse()

print(my_list)  # ['d', 'c', 'b', 'a']