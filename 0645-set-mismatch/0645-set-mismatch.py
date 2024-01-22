class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate, total_sum = 0, n * (n + 1) // 2  # Sum of 1 to n

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)
            total_sum -= num

        missing = total_sum + duplicate
        return [duplicate, missing]