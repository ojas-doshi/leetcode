class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Reverse half of the number and compare it with the other half
        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10

        # If the number of digits is odd, we can ignore the middle digit
        # For example, in 12321, after the loop, x will be 12 and reversed_num will be 123
        # So, we divide reversed_num by 10 to remove the last digit before comparison
        return x == reversed_num or x == reversed_num // 10