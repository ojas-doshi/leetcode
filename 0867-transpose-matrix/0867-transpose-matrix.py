class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        transposed_list = list()
        for i in range(len(matrix[0])):
            transposed_list.append([matrix[j][i] for j in range(len(matrix))])
        return transposed_list 
                