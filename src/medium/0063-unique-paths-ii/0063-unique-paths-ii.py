class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting point or ending point is an obstacle, there is no way to reach the destination
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # Initialize a 2D array to store the number of paths to each cell
        dp = [[0] * n for _ in range(m)]

        # Initialize the number of paths to the starting point
        dp[0][0] = 1

        # Fill the first column with the number of paths considering obstacles
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        # Fill the first row with the number of paths considering obstacles
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        # Calculate the number of paths for each cell considering obstacles
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # Return the number of paths to the bottom-right corner
        return dp[m - 1][n - 1]