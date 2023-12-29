class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        diff_list = list()

        i_size = len(grid)
        j_size = len(grid[0])
        
        j_0_1 = list()
        for j in range(j_size):
            j_row = [grid[i][j] for i in range(i_size)]
            j_0_1.append([j_row.count(0),j_row.count(1)])

        for i in range(i_size):
            onesRowi, zerosRowi = 0,0
            onesRowi = grid[i].count(1)
            zerosRowi = grid[i].count(0)
            i_row = list()
            for j in range(j_size):
                i_row.append(onesRowi + j_0_1[j][1] - zerosRowi - j_0_1[j][0])
            diff_list.append(i_row)
        
        return diff_list
        