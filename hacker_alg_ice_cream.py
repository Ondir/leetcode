m = 4
arr = [1, 4, 5, 3, 2]


def icecreamParlor(m, arr):
    inx = {}

    for i, v in enumerate(arr):
        temp = m - v
        if temp in inx:
            return [inx[temp], i]
        inx[v]=i



print(icecreamParlor(m, arr))