class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l,r = 1,length-2
        while l<=r:
            m = (r+l)//2
            left,right = mountainArr.get(m),mountainArr.get(m+1)
            pm = left<right
            if pm:
                l = m+1
            else:
                r = m
                break
        peak = r
        l,r = 0,peak-1
        while l<=r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val<target:
                l = m+1
            elif val>target:
                r = m -1
            else:
                return m
        l,r = peak,length-1
        while l<=r:
            m = (l+r)//2
            val = mountainArr.get(m)
            if val<target:
                r = m - 1
            elif val>target:
                l = m + 1
            else:
                return m
        return -1

        