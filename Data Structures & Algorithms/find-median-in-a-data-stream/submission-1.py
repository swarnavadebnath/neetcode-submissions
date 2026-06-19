import heapq as hp
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int) -> None:
        if self.minheap and num>self.minheap[0]:
            hp.heappush(self.minheap,num)
        else:
            hp.heappush(self.maxheap,-1*num)
        if len(self.minheap)>len(self.maxheap)+1:
            val = hp.heappop(self.minheap)
            hp.heappush(self.maxheap,-1*val)
        if len(self.minheap)+1<len(self.maxheap):
            val = -1*hp.heappop(self.maxheap)
            hp.heappush(self.minheap,val)

        

    def findMedian(self) -> float:
        size = len(self.minheap)+len(self.maxheap)
        if size%2==0:
            return (self.minheap[0]+(-1*self.maxheap[0]))/2.0
        elif len(self.minheap)>len(self.maxheap):
            return self.minheap[0]
        else:
            return -1*self.maxheap[0]
        
        