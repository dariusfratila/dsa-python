"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        length = k % len(nums)
        rev(0, len(nums) - 1)
        rev(0, length - 1)
        rev(length, len(nums) - 1)
