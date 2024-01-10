class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n > 0:
            n -= i
            i += 1
            if i > n:
                i-=1
                break
        return i
        
            