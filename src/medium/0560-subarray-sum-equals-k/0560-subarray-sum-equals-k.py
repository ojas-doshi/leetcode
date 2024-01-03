class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_count = {0: 1}  
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum - k in sum_count:
                count += sum_count[current_sum - k]

            sum_count[current_sum] = sum_count.get(current_sum, 0) + 1

        return count