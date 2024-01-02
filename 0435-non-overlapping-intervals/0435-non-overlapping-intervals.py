class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])  # Sort intervals by end time
        end = intervals[0][1]  # End time of the first interval
        removed_intervals = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:  # Overlapping interval found
                removed_intervals += 1
            else:
                end = intervals[i][1]  # Update the end time

        return removed_intervals