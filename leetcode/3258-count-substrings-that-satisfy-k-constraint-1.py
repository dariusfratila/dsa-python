"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        countMax = 0
        countZeros = 0
        countOnes = 0
        l = 0

        for r in range(len(s)):
            if s[r] == '0':
                countZeros += 1
            else:
                countOnes += 1

            while countZeros > k and countOnes > k:
                if s[l] == '0':
                    countZeros -= 1
                else:
                    countOnes -= 1
                l += 1

            countMax += (r - l + 1)

        return countMax
