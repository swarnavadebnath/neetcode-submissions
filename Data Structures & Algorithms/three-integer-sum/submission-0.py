class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                t=-nums[i]
                v=nums[j]+nums[k]
                if v>t:
                    k-=1
                elif v<t:
                    j+=1
                else:
                    l.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
        return l
                
                
        