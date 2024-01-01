class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        threshold = len(arr) // 4

        for i in range(len(arr)):
            if arr[i] == arr[i + threshold]:
                return arr[i]

        