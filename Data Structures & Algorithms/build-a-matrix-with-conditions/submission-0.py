class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def kahn(edges):
            indegree = [0]*(k+1)
            adj = [[] for _ in range(k+1)]
            for u,v in edges:
                adj[u].append(v)
                indegree[v]+=1
            order = []
            q = deque()
            for i in range(1,k+1):
                if not indegree[i]:
                    q.append(i)
            while q:
                node = q.popleft()
                order.append(node)
                for n in adj[node]:
                    indegree[n]-=1
                    if indegree[n] == 0:
                        q.append(n)
            return order
        row = kahn(rowConditions)
        if len(row) != k:
            return []
        col = kahn(colConditions)
        if len(col) != k:
            return []
        res = [[0]*k for _ in range(k)]
        colIndex = [0]*(k+1)
        for i in range(k):
            colIndex[col[i]] = i
        for i in range(k):
            res[i][colIndex[row[i]]] = row[i]
        return res
        