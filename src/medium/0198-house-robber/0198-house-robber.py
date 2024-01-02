class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Initialize variables to store the maximum amount robbed up to two houses ago and one house ago
        prev_house = 0
        curr_house = 0

        # Iterate through the houses to determine the maximum amount that can be robbed
        for num in nums:
            # Calculate the maximum amount that can be robbed at the current house
            temp = curr_house
            curr_house = max(prev_house + num, curr_house)
            prev_house = temp

        # Return the maximum amount that can be robbed
        return curr_house
