"""
@complexity
time: O(n)
space: O(n)
"""

class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result, left = 0, 0

        d = defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1
            while max(d.keys()) - min(d.keys()) > 2:
                d[nums[left]] -= 1
                if d[nums[left]] == 0:
                    del d[nums[left]]
                left += 1
            result += i - left + 1

        return result
