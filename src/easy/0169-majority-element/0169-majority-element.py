class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_set = set(nums)
        majority_num = 0
        counts = 0
        for num in nums_set:
            num_count = nums.count(num)
            if counts < num_count:
                majority_num = num
                counts = num_count
        return majority_num