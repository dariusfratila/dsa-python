"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index in range(len(nums)):
            if target - nums[index] in seen:
                return [seen[target - nums[index]], index]
            seen[nums[index]] = index
