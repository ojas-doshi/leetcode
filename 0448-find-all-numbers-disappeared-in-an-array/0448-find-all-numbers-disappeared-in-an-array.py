class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []

        # Mark elements as visited by flipping the sign of the number at index nums[i]
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        # Append indices of positive numbers to result (indices of missing elements)
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result