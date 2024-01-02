class Solution(object):
    count  = 0
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))  # Road from u to v
            graph[v].append((u, 0))  # Reversed road from v to u

        def dfs(node, prev):
            
            for neighbor, direction in graph[node]:
                if neighbor != prev:
                    self.count += direction  # Counting edges that need to be reversed
                    dfs(neighbor, node)

        self.count = 0
        dfs(0, -1)  # Start DFS from city 0
        return self.count