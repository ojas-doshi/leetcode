class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows, cols = len(grid), len(grid[0])
        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]

        def helper(row, col1, col2):
            if row == rows:
                return 0
            if col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
                return float('-inf')
            if dp[row][col1][col2] != -1:
                return dp[row][col1][col2]

            cherries = grid[row][col1]
            if col1 != col2:
                cherries += grid[row][col2]

            max_cherries = float('-inf')
            for new_col1 in [col1 - 1, col1, col1 + 1]:
                for new_col2 in [col2 - 1, col2, col2 + 1]:
                    max_cherries = max(max_cherries, helper(row + 1, new_col1, new_col2))

            dp[row][col1][col2] = cherries + max_cherries
            return dp[row][col1][col2]

        return max(0, helper(0, 0, cols - 1))
