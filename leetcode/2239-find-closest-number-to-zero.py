"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        closestNum = float('inf')
        for num in nums:
            if abs(num) < abs(closestNum):
                closestNum = num

        if closestNum < 0 and abs(closestNum) in nums:
            return abs(closestNum)

        return closestNum
