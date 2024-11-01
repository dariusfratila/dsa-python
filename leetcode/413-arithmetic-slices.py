"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 3:
            return 0

        count = 0
        streak = 0
        lastDiff = nums[1] - nums[0]

        for i in range(2, len(nums)):
            currentDifference = nums[i] - nums[i - 1]

            if currentDifference == lastDiff:
                streak += 1
                count += streak
            else:
                streak = 0

            lastDiff = currentDifference

        return count
