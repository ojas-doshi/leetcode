class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trust_count = [0] * (n + 1)

        for a, b in trust:
            trust_count[a] -= 1  # Person 'a' is not a judge
            trust_count[b] += 1  # Person 'b' is trusted

        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i

        return -1