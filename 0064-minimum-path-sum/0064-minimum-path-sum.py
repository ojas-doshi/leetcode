class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        # Initialize a 2D array to store the minimum path sum
        dp = [[0] * cols for _ in range(rows)]

        # Base case: initialize the first cell of dp
        dp[0][0] = grid[0][0]

        # Initialize the first row of dp
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # Initialize the first column of dp
        for j in range(1, cols):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # Fill the dp array using dynamic programming
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][cols - 1]