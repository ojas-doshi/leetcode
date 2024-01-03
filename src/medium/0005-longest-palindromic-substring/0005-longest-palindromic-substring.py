class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)  # Check for odd length palindrome
            len2 = self.expand_around_center(s, i, i + 1)  # Check for even length palindrome
            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
