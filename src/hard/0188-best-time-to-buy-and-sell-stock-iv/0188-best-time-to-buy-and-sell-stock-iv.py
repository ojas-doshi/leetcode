class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # If the number of transactions allowed is greater than half the length of the prices array,
        # it means you can buy and sell on every profitable day.
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit

        # Create two arrays to store the maximum profit with at most k transactions at each day
        dp_buy = [-float('inf')] * (k + 1)
        dp_sell = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                dp_buy[i] = max(dp_buy[i], dp_sell[i - 1] - price)
                dp_sell[i] = max(dp_sell[i], dp_buy[i] + price)

        return dp_sell[k]