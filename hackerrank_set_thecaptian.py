k = 5
list_of_room = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4, 3, 6, 8, 4, 3, 1, 5, 6, 2]

myset = set(list_of_room)


print(myset)
print(sum(myset))
print(sum(list_of_room))
print((sum(myset) * k))
print((sum(myset) * k) - (sum(list_of_room)))

print(((sum(myset) * k) - (sum(list_of_room))) // (k - 1))
