"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowels = set('aeiou')
        for word in range(left, right + 1):
            current_word = words[word]
            if current_word[0] in vowels and current_word[-1] in vowels:
                count += 1

        return count
