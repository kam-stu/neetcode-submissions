class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # default to buying the first
        buy = prices[0]
        l, r = 0, 1

        while r < len(prices):
            if prices[r] < buy:
                buy = prices[r]
                l = r
                r += 1
            else:
                max_profit = max(max_profit, prices[r] - buy)
                r += 1
            

        return max_profit