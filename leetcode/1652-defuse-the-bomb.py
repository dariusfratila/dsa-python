"""
@complexity
time: O(n)
space: O(n)
"""

class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        if k < 0:
            return self.decrypt(code[::-1], -k)[::-1]

        res = [0] * len(code)

        sumWindow = sum(code[:k])
        for index, value in enumerate(code):
            sumWindow += code[(index + k) % len(code)] - value
            res[index] = sumWindow

        return res
