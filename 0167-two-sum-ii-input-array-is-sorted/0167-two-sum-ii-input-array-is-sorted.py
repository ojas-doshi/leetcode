class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]  # adding 1 to convert to 1-indexed
            elif total < target:
                left += 1
            else:
                right -= 1

        # No solution found
        return [-1, -1]