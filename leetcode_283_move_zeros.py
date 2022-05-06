nums = [0, 3, 0, 1, 12]
pos = 0

for i, v in enumerate(nums):
    if v!=0:
        nums[i], nums[pos] = nums[pos], nums[i]
        pos+=1

print(nums)

