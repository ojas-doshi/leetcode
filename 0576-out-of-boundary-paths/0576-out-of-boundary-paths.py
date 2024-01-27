class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[[0] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for move in range(1, maxMove + 1):
            for i in range(m):
                for j in range(n):
                    for d in directions:
                        ni, nj = i + d[0], j + d[1]
                        if ni < 0 or ni >= m or nj < 0 or nj >= n:
                            dp[i][j][move] += 1  # Ball goes out of boundary
                        else:
                            dp[i][j][move] = (dp[i][j][move] + dp[ni][nj][move - 1]) % MOD

        return dp[startRow][startColumn][maxMove]