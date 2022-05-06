b = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

d = set([10, 1, 2, 3, 11, 21, 55, 6, 8, 9])
print(len(b)+len(d))
print(len(b.difference(d)))
print(b.difference(d))
print(len(d.difference(b)))
print(d.difference(b))
print(len(d.symmetric_difference(b)))
print(len(b)+len(d)-len(b.difference(d))-len(d.difference(b)))


print(len(b.union(d)))



1 2 3 6 5
4 4 2 5 3
6 1 6 5 3
2 4 1 2 5
1 4 3 6 8
4 3 1 5 6
2