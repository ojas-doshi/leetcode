class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort the intervals based on the start times
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            previous_start, previous_end = merged[-1]

            if current_start <= previous_end:
                # Merge the intervals
                merged[-1] = [previous_start, max(previous_end, current_end)]
            else:
                # Add a new interval
                merged.append([current_start, current_end])

        return merged