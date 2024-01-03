class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Create a Counter for characters in t
        target_counts = Counter(t)
        required = len(target_counts)

        left = 0
        right = 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None

        while right < len(s):
            # Expand the window by moving the right pointer
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            # Try to minimize the window by moving the left pointer
            while left <= right and formed == required:
                char = s[left]

                # Update the minimum window size
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # Shrink the window from the left
                window_counts[char] -= 1
                if char in target_counts and window_counts[char] < target_counts[char]:
                    formed -= 1
                left += 1

            # Move the right pointer to expand the window further
            right += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]