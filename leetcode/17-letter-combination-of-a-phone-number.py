"""
@complexity
time: O(4^n)
space: O(4^n)
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digits_hash = {'2': 'abc',
                       '3': 'def',
                       '4': 'ghi',
                       '5': 'jkl',
                       '6': 'mno',
                       '7': 'pqrs',
                       '8': 'tuv',
                       '9': 'wxyz'}

        def backtrack(index, current_list):
            if len(current_list) == len(digits):
                result.append(current_list)
                return

            for char in digits_hash[digits[index]]:
                backtrack(index + 1, current_list + char)

        if digits:
            backtrack(0, "")

        return result
