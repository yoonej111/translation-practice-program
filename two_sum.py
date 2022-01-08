from typing import List


nums = [2,7,11,15]
target = 22

print(range(0, len(nums)))
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return(i, j)
            

        



print(twoSum(nums, target))