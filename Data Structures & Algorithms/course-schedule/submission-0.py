class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for node1,node2 in prerequisites:
            adj[node1].append(node2)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if adj[node] == []:
                return True
            visited.add(node)
            for n in adj[node]:
                if not dfs(n):
                    return False
            visited.remove(node)
            adj[node] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        