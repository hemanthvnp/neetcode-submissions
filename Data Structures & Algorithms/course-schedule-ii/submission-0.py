class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
        path = set()
        visited = set()
        result = []
        def dfs(i):
            if i in path:
                return False
            if i in visited:
                return True
            path.add(i)
            for pre in graph[i]:
                if not dfs(pre):
                    return False

            path.remove(i)
            visited.add(i)
            result.append(i)

            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result

