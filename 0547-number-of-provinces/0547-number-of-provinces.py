class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        provinces = 0
        visited = [False] * n

        # Iterate through each city
        for i in range(n):
            if not visited[i]:
                # If the city hasn't been visited, start DFS to find the province
                self.dfs(isConnected, visited, i)
                provinces += 1

        return provinces
    
    def dfs(self, isConnected, visited, i):
        # Mark the current city as visited
        visited[i] = True

        # Traverse the adjacency matrix to find connected cities
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and not visited[j]:
                self.dfs(isConnected, visited, j)
