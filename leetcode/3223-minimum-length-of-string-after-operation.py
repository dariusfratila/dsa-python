"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        result = 0

        for count in Counter(s).values():
            if count % 2 == 1:
                result += 1
            else:
                result += 2

        return result
