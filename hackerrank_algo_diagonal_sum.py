from operator import mod

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

k = 0
j = 0
p = len(arr)-1

for i in range(len(arr)):
    k+=arr[i][i]
    j+=arr[i][p]
    p-=1
print(abs(k-j))
