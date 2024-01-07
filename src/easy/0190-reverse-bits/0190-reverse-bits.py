class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize the result to 0
        result = 0

        # Iterate through 32 bits
        for _ in range(32):
            # Shift the result to the left to make space for the next bit
            result <<= 1
            # Get the least significant bit of the input and add it to the result
            result |= n & 1
            # Shift the input to the right to process the next bit
            n >>= 1

        return result