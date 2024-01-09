class NumArray:
    def __init__(self, nums):
        self.cumulative_sums = [0]
        total = 0
        for num in nums:
            total += num
            self.cumulative_sums.append(total)

    def sumRange(self, left, right):
        return self.cumulative_sums[right + 1] - self.cumulative_sums[left]
