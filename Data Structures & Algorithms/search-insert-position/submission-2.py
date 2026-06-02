class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res=len(nums)
        l=0
        r=len(nums)-1
        while l<=r:
            m=l+((r-l)//2)
            if nums[m]>target:
                res=m
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                return m
        return res
        