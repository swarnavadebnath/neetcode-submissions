class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        def dfs(i,total):
            if i == len(nums):
                return total == target
            count = dfs(i+1,total+nums[i]) + dfs(i+1,total-nums[i])
            return count
        return dfs(0,0)
            

        
        