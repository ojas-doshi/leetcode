class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flips = 0
        while a > 0 or b > 0 or c > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            # Check if the current bits satisfy the condition a | b == c
            if (bit_a | bit_b) != bit_c:
                # Increment flips based on the required changes for each bit
                if bit_c == 0:
                    flips += bit_a + bit_b  # Both bits need to be flipped
                else:
                    flips += 1  # Only one bit needs to be flipped

            # Right shift all numbers to check the next bits
            a >>= 1
            b >>= 1
            c >>= 1

        return flips