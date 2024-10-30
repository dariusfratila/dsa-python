"""
@complexity
time: O(n^2)
space: O(1)
"""


class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_xor = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y):
                    max_xor = max(max_xor, x ^ y)

        return max_xor
