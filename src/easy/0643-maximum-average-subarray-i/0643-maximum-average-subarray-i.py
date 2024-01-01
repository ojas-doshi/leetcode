class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize variables for the initial window sum and the maximum average
        window_sum = sum(nums[:k])
        max_average = window_sum / k

        # Start iterating from index k to the end of the array
        for i in range(k, len(nums)):
            # Calculate the window sum by subtracting the element leaving the window and adding the new element
            window_sum += nums[i] - nums[i - k]
            # Update the maximum average if the current average is greater
            max_average = max(max_average, window_sum / k)

        return max_average