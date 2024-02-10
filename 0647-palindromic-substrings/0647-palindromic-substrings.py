class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):
            # Counting palindromic substrings with odd length
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            # Counting palindromic substrings with even length
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count
