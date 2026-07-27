class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        i = 0
        for a,b in equations:
            adj[a].append((b,values[i]))
            adj[b].append((a,1/values[i]))
            i+=1
        def dfs(node,target,visit):
            if node not in adj or target not in adj:
                return -1
            if node == target:
                return 1
            visit.add(node)
            for n,weight in adj[node]:
                if n not in visit:
                    res = dfs(n,target,visit)
                    if res != -1:
                        return weight * res
            return -1
        arr = []
        for q in queries:
            arr.append(dfs(q[0],q[1],set()))
        return arr

            
