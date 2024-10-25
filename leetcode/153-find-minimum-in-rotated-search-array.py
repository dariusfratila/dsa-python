"""
@complexity
time: O(log n)
space: O(1)
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        currMin = float('inf')
        while l <= r:
            m = (l + r) // 2

            currMin = min(currMin, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return min(currMin, nums[l])
