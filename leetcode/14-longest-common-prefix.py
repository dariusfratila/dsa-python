"""
@complexity
time: O(n * m)
space: O(1)
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length_string = float('inf')

        for s in strs:
            if len(s) < min_length_string:
                min_length_string = len(s)

        i = 0
        while i < min_length_string:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1

        return s[:i]
