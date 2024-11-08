"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        res = []

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                res.append(left_square)
                left += 1
            else:
                res.append(right_square)
                right -= 1

        res.reverse()
        return res
