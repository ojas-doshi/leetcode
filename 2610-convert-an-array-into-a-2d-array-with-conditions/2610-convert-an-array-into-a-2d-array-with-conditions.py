class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort(reverse=True) 
        result = []

        while nums:
            row = [nums.pop(0)] 
            i = 0
            while i < len(nums):
                if nums[i] not in row: 
                    row.append(nums.pop(i))
                else:
                    i += 1
            result.append(row)

        return result 
