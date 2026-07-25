class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visit = set()
        c = 0
        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        def dfs(node):
            visit.add(node)
            for n in adj[node]:
                if n not in visit:
                    dfs(n)
        for i in range(n):
            if i not in visit:
                c+=1
                dfs(i)
        return c

        