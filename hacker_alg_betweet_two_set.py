
def getTotalX(a, b):
    # Write your code here
    j = 1
    f = []
    for i in b:
        if i%j==0:
            print(i)
        j+=1

a = [2, 4]
b = [16, 32, 96]

print(getTotalX(a, b))
