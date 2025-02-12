"""
@complexity
time: O(n^2)
space: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result_string = ""
        result_length = 0

        for index in range(len(s)):
            left, right = index, index
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > result_length:
                    result_string = s[left: right + 1]
                    result_length = (right - left) + 1
                left -= 1
                right += 1

            left, right = index, index + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > result_length:
                    result_string = s[left: right + 1]
                    result_length = (right - left) + 1
                left -= 1
                right += 1

        return result_string
