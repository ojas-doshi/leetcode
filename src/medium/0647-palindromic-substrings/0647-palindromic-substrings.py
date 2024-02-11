class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        # Function to expand around center and count palindromic substrings
        def expand_around_center(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for i in range(n):
            # For odd length palindromes
            expand_around_center(i, i)
            # For even length palindromes
            expand_around_center(i, i + 1)

        return count