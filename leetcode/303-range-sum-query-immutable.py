"""
@complexity
time: O(n)
space: O(n)
"""


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        current = 0
        for i in nums:
            current += i
            self.prefix.append(current)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum
