class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2 = len(s1), len(s2)

        # If the total length of s1 and s2 is not equal to s3, return False
        if len1 + len2 != len(s3):
            return False

        # Create a DP array to store whether valid interleaving exists
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]

        # Base case initialization
        dp[0][0] = True

        # Fill the DP array
        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i > 0:
                    # Check if s1 matches with s3 and previous characters of s1 and s3 form an interleaving
                    dp[i][j] |= (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
                if j > 0:
                    # Check if s2 matches with s3 and previous characters of s2 and s3 form an interleaving
                    dp[i][j] |= (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

        return dp[len1][len2]