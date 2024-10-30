"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = {}
        maxWindow = float('-inf')
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while count[s[r]] > 2:
                count[s[l]] -= 1
                l += 1

            maxWindow = max(maxWindow, r - l + 1)

        return maxWindow
