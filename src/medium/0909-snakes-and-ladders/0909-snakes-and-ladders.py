class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n

        def get_coordinates(square):
            r, c = divmod(square - 1, n)
            if r % 2 == 1:  # Reverse direction for odd rows
                c = n - 1 - c
            return n - 1 - r, c

        moves = {1: 0}
        queue = deque([1])

        while queue:
            square = queue.popleft()
            if square == target:
                return moves[square]

            for i in range(1, 7):
                next_square = min(square + i, target)
                row, col = get_coordinates(next_square)

                if board[row][col] != -1:
                    next_square = board[row][col]

                if next_square not in moves:
                    moves[next_square] = moves[square] + 1
                    queue.append(next_square)

        return -1
