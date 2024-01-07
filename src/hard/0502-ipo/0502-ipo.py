class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(zip(capital, profits))

        available = []
        idx = 0

        for _ in range(k):
            while idx < n and projects[idx][0] <= w:
                heapq.heappush(available, -projects[idx][1])  # Store negative profits to use as max heap
                idx += 1

            if available:
                w -= heapq.heappop(available)  # Select the project with maximum profit
            else:
                break

        return w
