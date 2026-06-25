class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ar=0
        lm=height[l]
        rm=height[r]
        while l<r:
            if lm<rm:
                l+=1
                lm=max(lm,height[l])
                ar+=lm-height[l]
            else:
                r-=1
                rm=max(rm,height[r])
                ar+=rm-height[r]
        return ar



       




        