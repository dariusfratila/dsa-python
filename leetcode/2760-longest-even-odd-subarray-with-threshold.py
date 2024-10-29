"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        maxWindow = 0
        i = 0
        while i < len(nums):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                j = i + 1
                while j < len(nums) and nums[j] <= threshold and nums[j] % 2 != nums[j - 1] % 2:
                    j += 1
                maxWindow = max(maxWindow, j - i)
                i = j
            else:
                i += 1

        return maxWindow
