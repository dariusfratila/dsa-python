"""
@complexity
time: O(n)
space: O(n)
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        res, seen = set(), set()

        for i in range(len(s) - 9):
            window = s[i: i+10]
            if window in seen:
                res.add(window)
            seen.add(window)

        return list(res)
