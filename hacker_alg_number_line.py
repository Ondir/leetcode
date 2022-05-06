def kangaroo(x1, v1, x2, v2):

    j = 0
    k = 0
    while x1 <= x2:
        print(x1, x2)
        x1+=v1
        x2+=v2
        if x1>x2:
            return "No"
        elif x1 == x2:
            return "Yes"


x1, v1, x2, v2 = 0, 3, 4, 2

while x1 < x2:
    print(x1, x2)
    x1 += v1
    x2 += v2
    if x1 > x2:
        print("No")
    elif x1 == x2:
        print(x1,x2)
        print("Yes")

