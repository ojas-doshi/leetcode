class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')  # Initialize variables to store three distinct maximums

        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second and num < first:
                third = second
                second = num
            elif num > third and num < second:
                third = num

        # Check if the third distinct maximum exists, otherwise return the maximum number
        return third if third != float('-inf') else first
