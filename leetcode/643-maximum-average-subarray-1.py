"""
@complexity
time: O(n)
space: O(1)
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        sumWindow = sum(nums[:k])

        maxAverage = sumWindow / float(k)

        for r in range(k, len(nums)):
            sumWindow += nums[r] - nums[r - k]
            maxAverage = max(maxAverage, sumWindow / float(k))

        return maxAverage
