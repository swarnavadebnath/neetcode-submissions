class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        s=0
        res=999999
        while r<len(nums):
            s+=nums[r]
            while s>=target:
                res = min(r-l+1,res)
                s-=nums[l]
                l+=1
            r+=1
        if res==999999:
            return 0
        else:
            return res



        