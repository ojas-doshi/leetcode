class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)

        # Build the graph
        for (num, denom), value in zip(equations, values):
            graph[num][denom] = value
            graph[denom][num] = 1 / value

        def dfs(start, end, visited):
            # If start or end variable not in graph
            if start not in graph or end not in graph:
                return -1.0

            # If the start variable is the same as the end variable
            if start == end:
                return 1.0

            visited.add(start)
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result

            return -1.0

        results = []
        for query in queries:
            start, end = query
            results.append(dfs(start, end, set()))

        return results