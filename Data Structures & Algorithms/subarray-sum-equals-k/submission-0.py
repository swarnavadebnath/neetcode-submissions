class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        s=0
        d={0:1}
        for n in nums:
            s+=n
            diff = s-k
            if diff in d:
                cnt+=d[diff]
            d[s]=1+d.get(s,0)
        return cnt



    

        
        