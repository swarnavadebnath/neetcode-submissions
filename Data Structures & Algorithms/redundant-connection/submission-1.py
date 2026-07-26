class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        no = len(edges)
        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        visit = [False] * (no+1)
        cycle = set()
        cycstrt = -1
        def dfs(node,par):
            nonlocal cycstrt
            if visit[node]:
                cycstrt = node
                return True
            visit[node] = True
            for n in adj[node]:
                if n == par:
                    continue
                if dfs(n,node):
                    if cycstrt != -1:
                        cycle.add(node)
                        if node == cycstrt:
                            cycstrt = -1
                    return True
            return False
        dfs(1,-1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        return []

        
        