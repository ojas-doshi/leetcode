class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = 1
        duplicate = False

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                if not duplicate:
                    nums[count] = nums[i]
                    count += 1
                    duplicate = True
            else:
                nums[count] = nums[i]
                count += 1
                duplicate = False

        return count