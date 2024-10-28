"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """

        count = 0
        stringNum = str(num)
        for r in range(len(stringNum) - k + 1):
            substring = int(stringNum[r: r + k])
            if substring != 0 and num % substring == 0:
                count += 1

        return count
