"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s)
        while index == '':
            index -= 1

        count = 0
        while index != '':
            index -= 1
            count += 1

        return count
