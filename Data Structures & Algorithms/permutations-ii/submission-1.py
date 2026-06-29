class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        check = [False] * len(nums)
        def dfs(sub):
            if len(sub)==len(nums):
                res.append(sub.copy())
                return
            for i in range(len(nums)):
                if check[i]:
                    continue
                if i>0 and nums[i] == nums[i-1] and not check[i-1]:
                    continue       
                sub.append(nums[i])
                check[i] = True
                dfs(sub)
                sub.pop()
                check[i] = False
        dfs([])
        return res