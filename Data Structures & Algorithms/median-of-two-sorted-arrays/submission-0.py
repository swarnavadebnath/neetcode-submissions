class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=nums1+nums2
        m.sort()
        n=len(m)
        if n%2==0:
            return (m[(n//2)-1]+m[(n//2)])/2.0
        else:
            return m[n//2]

        
        