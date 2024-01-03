class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        piles = []

        for num in nums:
            # Binary search to find the pile where the current number can be placed
            left, right = 0, len(piles)
            while left < right:
                mid = (left + right) // 2
                if piles[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            # If no pile found, create a new pile
            if left == len(piles):
                piles.append(num)
            else:
                piles[left] = num

        return len(piles)