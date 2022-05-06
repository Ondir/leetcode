total = set()
nums = [-1, 0, 1, 2, -1, -4]
nums = sorted(nums)
print(nums)

for i, v in enumerate(nums):
    target = -nums[i]
    if v > 0:
        break
    k = i+1
    j = len(nums) - 1
    while k<j:
        if nums[k]+nums[j]<target:
            k+=1
        elif nums[k]+nums[j]>target:
            j-=1
        else:
            total.add((nums[i], nums[k], nums[j]))
            i+=1
            j-=1
    return total



