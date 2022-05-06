nums = [7,1,5,3,6,4]

total = 0
k = 0

for i in range(1, len(nums)):

    if nums[k]<nums[i]:
        total+=nums[i]-nums[k]
    k+=1


print(total)
