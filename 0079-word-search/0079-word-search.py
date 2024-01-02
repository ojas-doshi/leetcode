class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False

        def backtrack(row, col, word_index):
            # If the entire word is matched
            if word_index == len(word):
                return True

            # Check for out-of-bound indices or mismatching characters
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[word_index]:
                return False

            # Mark the current cell as visited
            temp = board[row][col]
            board[row][col] = '#'

            # Explore adjacent cells
            found = (backtrack(row + 1, col, word_index + 1) or
                     backtrack(row - 1, col, word_index + 1) or
                     backtrack(row, col + 1, word_index + 1) or
                     backtrack(row, col - 1, word_index + 1))

            # Restore the cell value before returning
            board[row][col] = temp
            return found

        # Iterate through the board cells
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True

        return False
