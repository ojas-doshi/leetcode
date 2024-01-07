class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_valid(row):
                return False

        # Check columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.is_valid(column):
                return False

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[r][c] for r in range(i, i + 3) for c in range(j, j + 3)]
                if not self.is_valid(sub_box):
                    return False

        return True

    def is_valid(self, arr):
        seen = set()
        for elem in arr:
            if elem != '.':
                if elem in seen:
                    return False
                seen.add(elem)
        return True