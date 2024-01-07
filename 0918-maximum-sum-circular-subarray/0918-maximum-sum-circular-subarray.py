class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Calculate maximum subarray sum using Kadane's algorithm
        def kadane(arr):
            max_sum = float('-inf')
            curr_sum = 0
            for num in arr:
                curr_sum = max(num, curr_sum + num)
                max_sum = max(max_sum, curr_sum)
            return max_sum

        total_sum = sum(nums)
        max_without_wrap = kadane(nums)

        # Calculate maximum subarray sum with circular wrapping
        # The circular maximum sum would be total sum minus the minimum subarray sum
        # because excluding the minimum subarray sum from total sum gives the maximum subarray sum
        for i in range(len(nums)):
            nums[i] = -nums[i]

        max_with_wrap = total_sum + kadane(nums)

        # If all numbers are negative, return the maximum without wrap
        if max_with_wrap == 0:
            return max_without_wrap

        return max(max_without_wrap, max_with_wrap)
