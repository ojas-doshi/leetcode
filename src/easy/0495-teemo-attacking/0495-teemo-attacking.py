class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total_duration = duration
        for i in range(1, len(timeSeries)):
            time_gap = timeSeries[i] - timeSeries[i - 1]
            total_duration += min(time_gap, duration)

        return total_duration