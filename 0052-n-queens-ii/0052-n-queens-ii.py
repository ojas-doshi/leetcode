class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(row, col):
            # Check if the current position is attacked by any previously placed queens
            for i in range(row):
                # Check if there is a queen in the same column or diagonals
                if board[i] == col or abs(row - i) == abs(col - board[i]):
                    return False
            return True

        def backtrack(row):
            nonlocal count
            if row == n:
                # If all queens are placed, increment the count of solutions
                count += 1
                return
            for col in range(n):
                if is_safe(row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1

        count = 0
        board = [-1] * n  # Initialize the chessboard
        backtrack(0)  # Start the backtracking process
        return count
