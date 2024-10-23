"""
@complexity
time: O(n^3)
space: O(n)
*using sliding window -> O(n^3)
*divide&conquer -> O(nlogn)
"""

class Solution(object):
    def isNice(self, s):
        uniqueChars = set(s)
        for char in uniqueChars:
            if char.lower() not in uniqueChars or char.upper() not in uniqueChars:
                return False

        return True

    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest = ""
        for left in range(len(s)):
            chars = set()
            for right in range(left, len(s)):
                chars.add(s[right])
                if self.isNice(chars):
                    if right - left + 1 > len(longest):
                        longest = s[left:right + 1]

        return longest
