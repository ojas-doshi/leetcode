class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col, queens):
            for r, c in queens:
                if col == c or row - col == r - c or row + col == r + c:
                    return False
            return True

        def backtrack(row, queens, result):
            if row == n:
                result.append([''.join('Q' if (r, c) in queens else '.' for c in range(n)) for r in range(n)])
                return
            for col in range(n):
                if is_safe(row, col, queens):
                    queens.append((row, col))
                    backtrack(row + 1, queens, result)
                    queens.pop()

        result = []
        backtrack(0, [], result)
        return result