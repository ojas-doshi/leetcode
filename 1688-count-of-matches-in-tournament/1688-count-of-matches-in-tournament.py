class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while(n !=1):
            matches = n // 2
            count = count + matches
            n = n - matches
        return count