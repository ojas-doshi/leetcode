class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        cur_end = 0 
        cur_farthest = 0

        for i in range(n - 1):
            cur_farthest = max(cur_farthest, i + nums[i])

            if i == cur_end:
                jumps += 1
                cur_end = cur_farthest

        return jumps