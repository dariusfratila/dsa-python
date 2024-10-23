"""
@complexity
time: O(n)
space: O(n)
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        seen = set()

        for i in range(len(nums)):
            if i > k:
                seen.remove(nums[i - k - 1])

            if nums[i] in seen:
                return True

            seen.add(nums[i])

        return False
