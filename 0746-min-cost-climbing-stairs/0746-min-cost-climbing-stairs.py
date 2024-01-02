class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        # Initialize the base cases
        dp[0] = cost[0]
        dp[1] = cost[1]

        # Calculate the minimum cost to reach each step
        for i in range(2, n + 1):
            if i < n:
                dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
            else:
                dp[i] = min(dp[i - 1], dp[i - 2])

        return dp[n]
