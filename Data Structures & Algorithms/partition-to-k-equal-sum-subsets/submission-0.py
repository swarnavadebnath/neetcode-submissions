class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        s = [0]*k
        target = sum(nums)//k
        def dfs(i):
            if i>=len(nums):
                return True
            for j in range(k):
                if nums[i]+s[j]>target:
                    continue
                
                if j>0 and s[j]==s[j-1]:
                 continue
                s[j]+=nums[i]
                if dfs(i+1):
                    return True
                s[j]-=nums[i]
            return False
        return dfs(0)
        