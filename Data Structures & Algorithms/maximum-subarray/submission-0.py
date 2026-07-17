class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cur = 0
        for n in nums:
            if cur<0:
                cur = 0
            cur +=n
            maxsum = max(maxsum,cur)
        return maxsum

        