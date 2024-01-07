class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        if len(points) <= 2:
            return len(points)

        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        max_points = 0

        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicate_points = 1  # Counter for points with the same coordinates
            for j in range(len(points)):
                if i != j:
                    if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                        duplicate_points += 1
                    else:
                        dx = points[j][0] - points[i][0]
                        dy = points[j][1] - points[i][1]
                        d = gcd(dx, dy)
                        slope = (dx // d, dy // d)
                        slopes[slope] += 1

            if not slopes:  # All points are duplicates
                max_points = max(max_points, duplicate_points)
            else:
                max_points = max(max_points, max(slopes.values()) + duplicate_points)

        return max_points