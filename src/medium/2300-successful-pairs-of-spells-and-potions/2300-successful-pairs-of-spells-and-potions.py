class Solution(object):
    def successfulPairs(self, spells, potions , success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        max_ans = []
        for i in range(len(spells)):
            s = 0
            e = len(potions) - 1
            ans = -1
            while s <= e:
                mid = s + (e - s) // 2
                value = potions[mid] * spells[i]
                if value >= success:
                    ans = mid
                    e = mid - 1
                else:
                    s = mid + 1
            if ans != -1:
                max_ans.append(len(potions) - ans)
            else:
                max_ans.append(0)
        return max_ans