"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) < 3:
            return 0

        count = 0
        for i in range(len(s)):
            substring = s[i:i+3]

            if len(set(substring)) == 3:
                count += 1

        return count
