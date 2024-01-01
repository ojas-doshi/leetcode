class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        special_pos_count = 0
        j_size = len(mat[0])
        j_counts = list()
        for j in range(j_size):
            j_counts.append([mat[i][j] for i in range(len(mat))].count(1))
            
        for i in range(len(mat)):
            i_count = mat[i].count(1)
            for j in range(j_size):
                special_pos_count += (mat[i][j] == 1 and j_counts[j] == 1 and i_count == 1 )
        return special_pos_count