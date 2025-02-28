"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profitProgress = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                profitProgress += profit
            l = r
            r += 1

        return profitProgress
