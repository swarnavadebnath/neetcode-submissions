class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [l for l in range(1,n+1)]
        res = []
        def dfs(i,sub):
            if len(sub) == k:
                res.append(sub.copy())
                return
            for j in range(i,len(nums)):
                sub.append(nums[j])
                dfs(j+1,sub)
                sub.pop()
        dfs(0,[])
        return res

        