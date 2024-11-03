"""
@compelxity
time: O(n)
space: O(1)
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k < 1:
            return 0

        totalCount = 0
        product = 1

        res = 0
        left = 0
        for right in range(len(nums)):
            product *= nums[right]

            while left <= right and product >= k:
                product //= nums[left]
                left += 1

            res += (right - left + 1)
            right += 1

        return res
