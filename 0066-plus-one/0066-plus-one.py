class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Iterate from right to left
        for i in range(n - 1, -1, -1):
            # Increment the current digit by 1
            digits[i] += 1

            # If there's no carry, return the updated digits
            if digits[i] < 10:
                return digits

            # If there's a carry, set the current digit to 0 and continue with the loop
            digits[i] = 0

        # If there's a carry after iterating through all digits, insert 1 at the beginning
        return [1] + digits
