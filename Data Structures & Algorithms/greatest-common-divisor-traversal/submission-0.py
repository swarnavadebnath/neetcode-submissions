class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        n = len(nums)
        visit = [False]*n
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                if gcd(nums[i],nums[j])>1:
                    adj[i].append(j)
                    adj[j].append(i)
        def dfs(node):
            visit[node] = True
            for pointer in adj[node]:
                if not visit[pointer]:
                    dfs(pointer)
        dfs(0)
        for node in visit:
            if not node:
                return False
        return True

        
        