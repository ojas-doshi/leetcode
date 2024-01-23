class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def is_unique(s):
            return len(s) == len(set(s))

        def backtrack(index, current):
            nonlocal max_length
            if is_unique(current):
                max_length = max(max_length, len(current))

            for i in range(index, len(arr)):
                backtrack(i + 1, current + arr[i])

        max_length = 0
        backtrack(0, "")
        return max_length