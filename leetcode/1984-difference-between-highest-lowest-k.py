"""
@complexity
time: O(nlogn)
space: O(1)
"""


class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        minDifference = float('inf')
        nums.sort()

        for index in range(len(nums) - k + 1):
            minDifference = min(
                minDifference, nums[index + k - 1] - nums[index])

        return minDifference
