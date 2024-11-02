"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(p) > len(s):
            return []

        countS, countP = {}, {}

        for i in range(len(p)):
            countP[p[i]] = 1 + countP.get(p[i], 0)
            countS[s[i]] = 1 + countS.get(s[i], 0)

        res = [0] if countP == countS else []

        l = 0
        for r in range(len(p), len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            countS[s[l]] -= 1
            if countS[s[l]] == 0:
                del countS[s[l]]

            l += 1
            if countS == countP:
                res.append(l)

        return res
