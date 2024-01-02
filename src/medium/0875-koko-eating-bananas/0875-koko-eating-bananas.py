class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def canFinish(speed):
            hours = 0
            for bananas in piles:
                hours += (bananas - 1) // speed + 1
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        return left
