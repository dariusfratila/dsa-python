"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pivot = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                pivot += 1
