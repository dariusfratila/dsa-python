
"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for i in numsSet:
            if i - 1 not in numsSet:
                length = 1
                while (i + length) in numsSet:
                    length += 1
                longest = max(length, longest)

        return longest
