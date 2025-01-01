"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            string_length = len(s)
            res += str(string_length) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            i = j + 1

            res.append(s[i:i + length])
            i += length

        return res
