class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n==1:
            return nums[0]
        curmax = nums[0]
        curmin = nums[0]
        res = nums[0]
        for i in range(1,n):
            a = nums[i] * curmax
            b = nums[i] * curmin
            curmax = max(nums[i],a,b)
            curmin = min(nums[i],a,b)
            res = max(res,curmax)
        return res 
        