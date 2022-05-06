from typing import List


def removeElement(nums: List[int], val: int) -> int:
    return len(list(filter(lambda a: a != val, nums)))



nums = [3,2,2,3]
val = 3


print(removeElement(nums, val))

