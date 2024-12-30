"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums[:len(nums)] + nums[:len(nums)]
