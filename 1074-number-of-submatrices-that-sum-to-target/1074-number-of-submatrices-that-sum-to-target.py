
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        count = 0

        # Calculate the prefix sum for each row
        for row in matrix:
            for i in range(1, cols):
                row[i] += row[i - 1]

        # Iterate over all possible pairs of columns and use hashing
        for col1 in range(cols):
            for col2 in range(col1, cols):
                prefix_sum = {0: 1}
                current_sum = 0

                # Iterate over all rows to find submatrix sum
                for row in matrix:
                    current_sum += row[col2] - (row[col1 - 1] if col1 > 0 else 0)
                    count += prefix_sum.get(current_sum - target, 0)
                    prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

        return count