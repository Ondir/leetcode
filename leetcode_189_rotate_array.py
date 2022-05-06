import copy

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

k = k % len(nums)
print(k)
tmp = copy.copy(nums)
print(tmp)

nums[:k] = tmp[len(nums) - k:]
print(tmp[len(nums) - k:])

nums[k:] = tmp[:len(nums) - k]
print(tmp[:len(nums) - k])
print(nums)