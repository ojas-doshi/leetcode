class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        n = len(jobDifficulty)
        if n < d:
            return -1

        dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
        dp[0][0] = 0

        for day in range(1, d + 1):
            for job in range(1, n + 1):
                max_difficulty = 0
                for k in range(job, 0, -1):
                    max_difficulty = max(max_difficulty, jobDifficulty[k - 1])
                    dp[day][job] = min(dp[day][job], dp[day - 1][k - 1] + max_difficulty)

        return dp[d][n]