"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            med = numbers[l] + numbers[r]
            if target < med:
                r -= 1
            elif target > med:
                l += 1
            else:
                return [l + 1, r + 1]
