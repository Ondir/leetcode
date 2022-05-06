arr = [-4, 3, -9, 0, 4, 1]

total_len = len(arr)
positive = len(list(filter(lambda x: x<0, arr)))
negative = len(list(filter(lambda x: x>0, arr)))
zero = len(list(filter(lambda x: x==0, arr)))
print(round(positive/total_len, 6))
print(round(negative/total_len, 6))
print(round(zero/total_len, 6))