"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = new_max

        return arr
