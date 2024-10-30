"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """

        alternate = 0
        for i in range(len(colors)):
            if colors[i] != colors[(i + 1) % len(colors)] and colors[(i + 1) % len(colors)] != colors[(i + 2) % len(colors)]:
                alternate += 1

        return alternate
