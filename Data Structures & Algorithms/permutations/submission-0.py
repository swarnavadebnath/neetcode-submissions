class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(sub):
            if len(sub)==len(nums):
                res.append(sub.copy())
            for i in range(len(nums)):
                if nums[i] in sub:
                    continue
                sub.append(nums[i])
                dfs(sub)
                sub.pop()
        dfs([])
        return res
        