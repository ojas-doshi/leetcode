class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        # Define states to track maximum profit after each transaction at each day
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0

        for i in range(1, n):
            # Update the first buy and sell transactions
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])

            # Update the second buy and sell transactions
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])

        return sell2