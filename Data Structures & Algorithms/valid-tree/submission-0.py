class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>=n:
            return False
        adj = collections.defaultdict(list)
        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        visit = set()
        def dfs(node,par):
            if node in visit:
                return False
            visit.add(node)
            for n in adj[node]:
                if n == par:
                    continue
                if not dfs(n,node):
                    return False
            return True
        return dfs(0,-1) and len(visit) == n

        