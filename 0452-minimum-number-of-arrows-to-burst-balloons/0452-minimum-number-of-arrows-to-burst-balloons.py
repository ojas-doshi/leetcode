class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort the balloons based on their end points
        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        # Check for overlapping intervals and count the number of arrows needed
        for start, balloon_end in points:
            if start > end:
                arrows += 1
                end = balloon_end

        return arrows