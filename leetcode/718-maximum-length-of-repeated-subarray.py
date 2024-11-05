"""
@complexity
time: O(m * n)
space: O(1)
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        res = 0

        for i in range(m):
            left, length = 0, 0
            for j in range(n):
                if nums1[i + left] == nums2[j]:
                    length += 1
                    res = max(res, length)
                else:
                    length = 0
                left += 1
                if i + left == m:
                    break

        for j in range(n):
            left, length = 0, 0
            for i in range(m):
                if nums1[i] == nums2[j + left]:
                    length += 1
                    res = max(res, length)
                else:
                    length = 0
                left += 1
                if j + left == n:
                    break

        return res
