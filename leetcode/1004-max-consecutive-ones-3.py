"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, res, count_ones = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 1:
                count_ones += 1

            while right - left + 1 - count_ones > k:
                if nums[left] == 1:
                    count_ones -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
