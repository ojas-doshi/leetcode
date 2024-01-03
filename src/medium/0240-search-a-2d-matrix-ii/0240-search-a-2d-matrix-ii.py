class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1  # Starting from the top-right corner

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1  # Move down if the current element is smaller than the target
            else:
                col -= 1  # Move left if the current element is larger than the target

        return False