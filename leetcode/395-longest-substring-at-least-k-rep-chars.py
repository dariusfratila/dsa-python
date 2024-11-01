"""
@complexity
time: O(n * charSet)
space: O(charSet)
"""

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        charSet = len(set(s))
        resultMax = 0

        for currentChar in range(1, charSet + 1):
            counter = defaultdict(int)
            left = 0

            for right in range(len(s)):
                counter[s[right]] += 1
                while len(counter) > currentChar:
                    counter[s[left]] -= 1
                    if counter[s[left]] == 0:
                        del counter[s[left]]
                    left += 1

                greaterK = True
                for element in counter.values():
                    if element < k:
                        greaterK = False
                        break

                if greaterK:
                    resultMax = max(resultMax, right - left + 1)

        return resultMax
