import heapq as hp
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x,y in points:
            dis = x**2 + y**2
            hp.heappush(maxheap,(-dis,x,y))
            if len(maxheap)>k:
                hp.heappop(maxheap)
        res = []
        for dist,x,y in maxheap:
            res.append([x,y])
        return res
        