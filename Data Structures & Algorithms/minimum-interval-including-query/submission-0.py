class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minheap = []
        res = [-1] * len(queries)
        for i in range(len(queries)):
            queries[i] = (queries[i],i)
        queries.sort()
        i = 0
        for q in queries:
            while i<len(intervals) and intervals[i][0]<=q[0]:
                l,r = intervals[i]
                heapq.heappush(minheap,(r-l+1,r))
                i+=1
            while minheap and minheap[0][1]<q[0]:
                heapq.heappop(minheap)
            if minheap:
                res[q[1]] = minheap[0][0]
            else:
                res[q[1]] = -1
        return res 
        
