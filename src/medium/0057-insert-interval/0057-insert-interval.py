class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0
        n = len(intervals)

        # Add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1

        merged.append(newInterval)

        # Add remaining intervals
        while i < n:
            merged.append(intervals[i])
            i += 1

        return merged