class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k==len(arr):
            return arr
        r=k
        while r<len(arr):
            if abs(arr[r-k]-x)<=abs(arr[r]-x) and arr[r-1]!=arr[r]:
                break
            r+=1
        return arr[r-k:r]

        