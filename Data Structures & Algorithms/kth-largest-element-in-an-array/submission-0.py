import heapq as hp
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for i in range(len(nums)):
            hp.heappush(minheap,nums[i])
            if len(minheap)>k:
                hp.heappop(minheap)
        return minheap[0]


        