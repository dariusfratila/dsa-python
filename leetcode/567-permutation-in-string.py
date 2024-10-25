"""
@complexity
time: O(n)
space: O(1) - fixed alphabet size, O(n) for arbitrary characters
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        seen = {}
        countS1 = Counter(s1)

        for r in range(len(s2)):
            seen[s2[r]] = 1 + seen.get(s2[r], 0)

            if r - l + 1 > len(s1):
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l += 1

            if seen == countS1:
                return True

        return False
