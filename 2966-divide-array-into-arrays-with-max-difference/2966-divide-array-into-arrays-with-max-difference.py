class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
         # Sort the array
        nums.sort()

        n = len(nums)

        # Check if it is possible to divide the array
        for i in range(0, n, 3):
            if i + 2 >= n or nums[i + 2] - nums[i] > k:
                return []

        # Create arrays of size 3
        result = [nums[i:i+3] for i in range(0, n, 3)]

        return result