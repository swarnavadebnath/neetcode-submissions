class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=[]
        for i in range(k,len(nums)+1):
            s=nums[i-k:i]
            l.append(max(s))
        return l

        