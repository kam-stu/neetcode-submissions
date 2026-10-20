class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]

        for sell in prices:
            profit = sell - buy
            res = max(profit, res)
            buy = min(buy, sell)

        return res
