class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for a,b,t in times:
            adj[a].append((b,t))
        def bfs(graph,start):
            distance = {node:float('inf') for node in range(1,n+1)}
            distance[start] = 0
            queue = [(0,start)]
            while queue:
                cur_time,cur_node = heapq.heappop(queue)
                if cur_time>distance[cur_node]:
                    continue
                for nbr,t in graph[cur_node]:
                    time = cur_time + t
                    if time<distance[nbr]:
                        distance[nbr] = time
                        heapq.heappush(queue,(time,nbr))
            return distance
        res = bfs(adj,k)
        for k,v in res.items():
            if v == float('inf'):
                return -1
        return max(res.values())
        