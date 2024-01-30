class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def countNegatives(sub_list):
            return sum(ele < 0 for ele in sub_list)
        return sum(countNegatives(sub_list) for sub_list in grid)