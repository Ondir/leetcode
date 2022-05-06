from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    inx = {}
    for i, v in enumerate(nums):
        sum_ar = target - v
        if sum_ar in inx:
            return [inx[sum_ar], i]
        inx[v]=i

nums = [3,2,3]
target = 6

print(twoSum(nums, target))