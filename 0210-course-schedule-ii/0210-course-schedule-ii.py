class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create adjacency list and indegree count
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Initialize queue with courses having 0 indegree
        queue = deque([course for course in range(numCourses) if indegree[course] == 0])
        order = []

        # Perform topological sort
        while queue:
            curr_course = queue.popleft()
            order.append(curr_course)

            for next_course in graph[curr_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # Check if all courses can be taken
        if len(order) == numCourses:
            return order
        else:
            return []
