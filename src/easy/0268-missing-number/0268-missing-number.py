class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers using Gauss' formula
        actual_sum = sum(nums)
        return expected_sum - actual_sum