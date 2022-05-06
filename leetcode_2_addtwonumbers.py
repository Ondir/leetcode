l1 = [2,4,3]
l1 = l1[::-1]
print(l1)
l2 = [5,6,4]
l2 = l2[::-1]
print(l2)

num1 = ''.join([str(i) for i in l1])
num2 = ''.join([str(i) for i in l2])
total = int(num1)+ int(num2)
print([int(i) for i in str(total)])