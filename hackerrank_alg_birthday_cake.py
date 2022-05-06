arr = [3, 2, 1, 3]

max_arr = 0
count = 0

for i in arr:
    if i > max_arr:
        max_arr = i
        count = 1
    elif i == max_arr:
        count+=1

print(count)
