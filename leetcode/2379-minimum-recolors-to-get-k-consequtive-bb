"""
@complexity
time: O(n)
space: O(1)
"""


class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """

        countWhites = blocks[:k].count('W')
        minOperations = countWhites

        l = 0
        for r in range(k, len(blocks)):
            if blocks[l] == 'W':
                countWhites -= 1
            if blocks[r] == 'W':
                countWhites += 1

            minOperations = min(minOperations, countWhites)
            l += 1

        return minOperations
