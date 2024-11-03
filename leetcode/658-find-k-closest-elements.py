"""
@complexity sliding window
time: O(n)
space: O(k)

@complexity two pointers
time: O(n)
space: O(1)
"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        # sliding window

        # resArray = arr[:k]
        # l = 0

        # for r in range(k, len(arr)):
        #     differenceL = abs(arr[l] - x)
        #     differenceR = abs(arr[r] - x)

        #     if differenceL > differenceR:
        #         resArray.pop(0)
        #         resArray.append(arr[r])
        #         l += 1

        # return resArray

        # ----

        # two pointers

        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1

        return arr[l:r + 1]
