"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        minWindow = float('inf')
        sumWindow = 0

        for r in range(0, len(nums)):
            sumWindow += nums[r]
            while sumWindow >= target:
                minWindow = min(minWindow, r - l + 1)
                sumWindow -= nums[l]
                l += 1

        return minWindow if minWindow != float('inf') else 0
