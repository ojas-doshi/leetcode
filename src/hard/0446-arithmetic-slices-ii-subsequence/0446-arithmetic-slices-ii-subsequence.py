class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0  # Initialize the count of arithmetic subsequences

        # Create a list of dictionaries to store subsequences ending at each index
        dp = [{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]  # Calculate the difference between elements

                # Check if the arithmetic subsequence ending at j can be extended to i
                if diff in dp[j]:
                    dp[i][diff] = dp[i].get(diff, 0) + dp[j][diff]
                    total += dp[j][diff]  # Add the count of valid subsequences to total

                # If there's a pair of elements with the difference, add 1 (forming a 3-length subsequence)
                dp[i][diff] = dp[i].get(diff, 0) + 1

        return total