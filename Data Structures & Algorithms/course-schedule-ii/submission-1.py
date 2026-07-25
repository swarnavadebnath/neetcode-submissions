class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for node1,node2 in prerequisites:
            adj[node1].append(node2)
        res = []
        visited = set()
        cycle = set()
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for n in adj[node]:
                if not dfs(n):
                    return False
            cycle.remove(node)
            visited.add(node)
            res.append(node)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
        