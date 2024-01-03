class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        n = len(bank[0])
        positions = [[] for _ in range(m)]

        # Store positions of '1's in each row
        for i in range(m):
            for j in range(n):
                if bank[i][j] == '1':
                    positions[i].append(j)

        total_beams = 0

        # Check for valid laser beams between different rows
        for i in range(m):
            for j in range(i + 1, m):
                if len(positions[i]) == 0 or len(positions[j]) == 0:
                    continue

                valid_beam = True
                for k in range(i + 1, j):
                    if any(bank[k][col] == '1' for col in positions[k]):
                        valid_beam = False
                        break

                if valid_beam:
                    total_beams += len(positions[i]) * len(positions[j])

        return total_beams