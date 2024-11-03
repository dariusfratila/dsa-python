"""
@complexity
time: O(n)
space: O(k)
"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        resArray = arr[:k]
        l = 0

        for r in range(k, len(arr)):
            differenceL = abs(arr[l] - x)
            differenceR = abs(arr[r] - x)

            if differenceL > differenceR:
                resArray.pop(0)
                resArray.append(arr[r])
                l += 1

        return resArray
