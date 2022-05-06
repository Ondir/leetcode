nums = [1, 2, 3, 4, 5, 6, 8]
k = 3
for i in range(k):
    t = nums[-1]
    nums.insert(0, t)
    del nums[-1]

print(nums)