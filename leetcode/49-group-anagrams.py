"""
@complexity
time: O(n*m)
space: O(n*m)
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        hash = defaultdict(list)

        for string_variable in strs:
            count = [0] * 26
            for char in string_variable:
                count[ord(char) - ord('a')] += 1

            hash[tuple(count)].append(string_variable)

        return list(hash.values())
