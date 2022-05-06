test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]

i, j = 0, 0

total = []
l2 = len(test_list2)
l1 = len(test_list1)

while i < l1 and j < l2:
    if test_list1[i] < test_list2[j]:
        total.append(test_list1[i])
        i += 1
    else:
        total.append(test_list2[j])
        j += 1

print(total)