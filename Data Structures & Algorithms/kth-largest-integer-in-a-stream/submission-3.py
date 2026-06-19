import heapq as hp
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        hp.heapify(self.minheap)
        self.k = k
        while len(self.minheap)>k:
            hp.heappop(self.minheap)
        

        

    def add(self, val: int) -> int:
        hp.heappush(self.minheap,val)
        if len(self.minheap)>self.k:
            hp.heappop(self.minheap)
        return self.minheap[0]

        
