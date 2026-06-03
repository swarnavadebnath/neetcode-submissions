class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            sub=0
            curr=0
            for n in nums:
                curr+=n
                if curr>largest:
                    sub+=1
                    curr=n
            if 1+sub<=k:
                return True
            else:
                return False
        l=max(nums)
        r=sum(nums)
        res=r
        while l<=r:
            m = l+((r-l)//2)
            if canSplit(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res

        