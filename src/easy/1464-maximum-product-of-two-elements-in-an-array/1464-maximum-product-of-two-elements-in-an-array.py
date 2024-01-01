class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_elements1 = max(nums)
        nums.pop(nums.index(max_elements1))
        max_elements2 = max(nums)
        return (max_elements1 - 1) * (max_elements2 - 1)