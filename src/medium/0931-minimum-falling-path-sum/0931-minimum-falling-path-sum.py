class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        n = len(matrix)

        # Initialize dp array with the first row of the matrix
        dp = matrix[0][:]

        for i in range(1, n):
            # Create a new dp array for the current row
            new_dp = [0] * n
            for j in range(n):
                # Calculate the minimum falling path sum for the current element
                new_dp[j] = matrix[i][j] + min(dp[max(0, j - 1):min(n, j + 2)])

            # Update dp array with the new row
            dp = new_dp

        # Return the minimum value in the last row
        return min(dp)