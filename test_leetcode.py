nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
#Output: [8,6,2,4]


sum_nums = sum([i for i in nums if i%2==0])
print(sum_nums)

total_nums = []

for v, k in queries:
    if nums[k]%2 == 0:
        sum_nums-=nums[k]
    nums[k]+=v
    if nums[k]%2 == 0:
        sum_nums += nums[k]
    total_nums.append(sum_nums)
print(total_nums)
