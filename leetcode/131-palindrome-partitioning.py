"""
@complexity
time: O(n * 2^n)
space: O(n)
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []

        def backtrack(start_index, current_partition):
            if start_index == len(s):
                partitions.append(current_partition.copy())
                return

            for end_index in range(start_index, len(s)):
                if self.is_palindrome(start_index, end_index, s):
                    current_partition.append(s[start_index: end_index + 1])
                    backtrack(end_index + 1, current_partition)
                    current_partition.pop()

        backtrack(0, [])
        return partitions

    def is_palindrome(self, left, right, s):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
