class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for i in range(start, len(s)):
                if is_palindrome(s[start:i + 1]):
                    path.append(s[start:i + 1])
                    backtrack(i + 1, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result