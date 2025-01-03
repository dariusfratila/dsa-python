"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_length, word2_length = 0, 0
        res = []
        while word1_length < len(word1) and word2_length < len(word2):
            res.append(word1[word1_length])
            res.append(word2[word2_length])
            word1_length += 1
            word2_length += 1

        res.append(word1[word1_length:])
        res.append(word2[word2_length:])

        return ''.join(res)
