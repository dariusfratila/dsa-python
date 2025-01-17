"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        ans = []

        prefix = [0] * (len(words) + 1)
        res = [0] * (len(queries))

        prev = 0
        for index, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                prev += 1
            prefix[index + 1] = prev

        for index, query in enumerate(queries):
            print(query)
            left, right = query
            res[index] = prefix[right + 1] - prefix[left]

        return res
