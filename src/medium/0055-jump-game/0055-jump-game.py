class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False

        furthest = 0
        last_index = len(nums) - 1

        for i in range(len(nums)):
            if i > furthest:
                return False
            furthest = max(furthest, i + nums[i])
            if furthest >= last_index:
                return True

        return furthest >= last_index