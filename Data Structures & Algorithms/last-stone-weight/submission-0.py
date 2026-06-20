import heapq as hp
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap =  [-x for x in stones]
        hp.heapify(maxheap)
        while len(maxheap)>1:
            y = -1 * hp.heappop(maxheap)
            x = -1 * hp.heappop(maxheap)
            if x<y:
                hp.heappush(maxheap,x-y)
        if maxheap:
            return -1*maxheap[0]
        else:
            return 0

        