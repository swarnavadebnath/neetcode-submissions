class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for n1,n2,p in flights:
            adj[n1].append((n2,p))
        queue = [(0,0,src)]
        while queue:
            price,step,node = heapq.heappop(queue)
            if node == dst:
                return price
            for nbr,p in adj[node]:
                curprice = price + p
                if step<=k:
                    heapq.heappush(queue,(curprice,step+1,nbr))
        return -1
            
        
    
