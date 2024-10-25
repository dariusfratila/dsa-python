"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                print(prices[l], prices[r])
                l = r
            else:
                balance = prices[r] - prices[l]
                maxProfit = max(maxProfit, balance)
            r = r + 1

        return maxProfit
