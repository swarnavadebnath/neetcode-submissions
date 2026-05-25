class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            s = target - nums[i]
            if s in d and d[s]!=i:
                return [i,d[s]]

        