x,y,z,n = 2,2,2,2
total_arr = []
for a in range(0, x+1):
    print(a)
    for b in range(0, y+1):
        print(a, b)
        for c in range(0, z+1):
            if a+b+c != n:
                total_arr.append([a,b,c])
print(total_arr)

total_arr = [[a,b,c] for a in range(0,x+1) for b in range(0, y+1) for c in range(0,z+1) if a+b+c!=n ]
print(total_arr)