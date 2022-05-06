arr = [396285104, 573261094, 759641832, 819230764, 364801279]

sorted(arr)
print(arr)

min = sum([v for i, v in enumerate(sorted(arr)) if i != len(arr)-1])
max = sum([v for i, v in enumerate(sorted(arr)) if i != 0])
print(max)
print(min)
print(sorted(arr))

