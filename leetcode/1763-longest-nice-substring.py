"""
@complexity:
time: O(n)
space: O(n)
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0
        longest = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            windowSize = (r - l) + 1
            longest = max(longest, windowSize)

            seen.add(s[r])

        return longest
