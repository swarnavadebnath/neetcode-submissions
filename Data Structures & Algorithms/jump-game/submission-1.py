class Solution:
    def canJump(self, nums: List[int]) -> bool:
        FurthestReach = 0
        n = len(nums)
        for i in range(n):
            if i>FurthestReach:
                return False
            FurthestReach = max(FurthestReach,i+nums[i])
        return True

        