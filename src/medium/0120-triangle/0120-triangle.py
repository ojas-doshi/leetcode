class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1]  # Initialize the dp array with the bottom row

        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Update the dp array with the minimum sum path from the current row to the bottom
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0] 