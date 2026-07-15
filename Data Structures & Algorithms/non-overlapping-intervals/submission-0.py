class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c = 0
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
            else:
                c+=1
                end = min(end,intervals[i][1])
        return c 
        