"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev, curr = 0, 0

        for i in range(2, len(cost) + 1):
            prev, curr = curr, min(cost[i - 2] + prev, cost[i - 1] + curr)

        return curr
