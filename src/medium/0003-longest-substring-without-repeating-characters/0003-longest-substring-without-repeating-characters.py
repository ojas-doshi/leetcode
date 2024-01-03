class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_index = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_index:
                # Move the start of the window to the right of the last occurrence of the repeated character
                start = max(start, char_index[s[end]] + 1)

            # Update the index of the current character
            char_index[s[end]] = end
            # Update the maximum length of the substring without repeating characters
            max_length = max(max_length, end - start + 1)

        return max_length