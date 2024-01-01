class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_freq = {}
        count = 0

        for num in nums:
            complement = k - num
            if complement in num_freq and num_freq[complement] > 0:
                count += 1
                num_freq[complement] -= 1
            else:
                num_freq[num] = num_freq.get(num, 0) + 1

        return count