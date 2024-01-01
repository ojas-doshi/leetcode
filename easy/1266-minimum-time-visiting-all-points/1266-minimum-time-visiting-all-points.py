class Solution(object):
    
    def getChangePointPart(self,x,y):
        """
        :type x : int
        :type x : int        
        :rtype : int
        """
        if x == y:
            return 0
        elif x > y:
            return -1
        else:
            return 1
    
    def getCurrentPoint(self,curr_pt,change_pt):
        """
        :type curr_pt: list[int]
        :type change_pt: list[int]
        :rtype : list[int]
        """
        return [curr_pt[0]+change_pt[0],curr_pt[1]+change_pt[1]]
    
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count =  0
        for i in range(len(points)-1):
            pt1, pt2 = points[i], points[i+1]
            curr_pt = points[i]
            while curr_pt != pt2:
                change_pt = [
                    self.getChangePointPart(curr_pt[0], pt2[0]),
                    self.getChangePointPart(curr_pt[1], pt2[1])
                ]
                curr_pt = self.getCurrentPoint(curr_pt, change_pt)
                count = count + 1
        return count
                    
            