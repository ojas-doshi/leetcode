class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                # Update row[j] by adding row[j] and row[j - 1] from the previous row
                row[j] += row[j - 1]

        return row