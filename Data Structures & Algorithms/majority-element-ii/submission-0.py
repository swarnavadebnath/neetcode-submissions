class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h={}
        l=[]
        for i in range(len(nums)):
            val=nums[i]
            if val not in h:
                h[val] = 1
            else:
                h[val] += 1
        for k,v in h.items():
            if v>(len(nums)/3):
                l.append(k)
        return l
        