class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # Check if the first row should be zeroed
        for i in range(cols):
            if matrix[0][i] == 0:
                first_row_has_zero = True
                break

        # Check if the first column should be zeroed
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Use first row and first column to mark zeros
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set zeros based on markings in first row and column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set zeros for first row and first column if needed
        if first_row_has_zero:
            for i in range(cols):
                matrix[0][i] = 0

        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0