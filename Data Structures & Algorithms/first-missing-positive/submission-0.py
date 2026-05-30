class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=1
        for i in nums:
            if n in nums:
                n+=1
            else:
                break
        return n


        