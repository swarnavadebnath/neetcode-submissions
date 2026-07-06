class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n==1:
            return nums[0]
        def dp(house):
            r1,r2 = 0,0
            for money in house:
                temp = max(r1+money,r2)
                r1 = r2
                r2 = temp
            return r2
        return max(dp(nums[1:]),dp(nums[:n-1]))
        