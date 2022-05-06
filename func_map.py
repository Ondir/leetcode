list_ar = [1, 2, 3, 4, 5]

print(list(map(lambda x: x*2, list_ar)))

print([(lambda x: x * 2)(x) for x in list_ar])



p

