class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        degree = [0]*n
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[a]+=1
            degree[b]+=1
        queue = collections.deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        while n>2:
            count = len(queue)
            n -= count
            for _ in range(count):
                node = queue.popleft()
                for j in adj[node]:
                    degree[j]-=1
                    if degree[j] == 1:
                        queue.append(j)
        return list(queue)
        


        
        
        