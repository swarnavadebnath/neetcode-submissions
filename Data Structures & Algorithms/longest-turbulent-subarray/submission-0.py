class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if not arr:
            return 0
        l = 0
        r = 1
        res = 1
        d = 0
        while r<n:
            if arr[r-1]>arr[r]:
                cur = -1
            elif arr[r-1]<arr[r]:
                cur = 1
            else:
                cur = 0
            if cur != d and cur != 0:
                res = max(res,r-l+1)
            elif cur == 0:
                l = r
            else:
                l = r - 1
                res = max(res,r-l+1)
            r+=1
            d = cur
        return res
                
        