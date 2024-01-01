class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize an array to store the count of set bits
        bits_count = [0] * (n + 1)

        for i in range(1, n + 1):
            # Use i & (i - 1) to count the number of set bits in i
            bits_count[i] = bits_count[i >> 1] + (i & 1)

        return bits_count