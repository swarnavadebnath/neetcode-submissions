class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for node1,node2 in prerequisites:
            adj[node1].append(node2)
        pre = {}
        def dfs(node):
            if node not in pre:
                pre[node] = set()
                for n in adj[node]:
                    pre[node] |= dfs(n)
                pre[node].add(node)
            return pre[node]
        for c in range(numCourses):
            dfs(c)
        res = []
        for u,v in queries:
            res.append(v in pre[u])
        return res
