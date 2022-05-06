nums = sorted(set([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
rear=nums[0]
front=nums[0]
for i in range(1,len(nums)):
    rear=rear+nums[i]
    rear=max(nums[i],rear)
    front=max(rear,front)
print( front)

