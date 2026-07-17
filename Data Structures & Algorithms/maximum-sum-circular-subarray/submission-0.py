class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globmax,globmin = nums[0],nums[0]
        curmax,curmin,total = 0,0,0
        for n in nums:
            curmax = max(n,curmax+n)
            globmax = max(globmax,curmax)
            curmin = min(curmin+n,n)
            globmin = min(globmin,curmin)
            total+=n
        if globmax>0:
            return max(globmax,total-globmin)
        else:
            return globmax
        