class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        i = 0
        res = [intervals[0]]
        for c in intervals:
            if res[i][1] >= c[0]:
                res[i][1] = max(res[i][1],c[1])
            else:
                res.append(c)
                i+=1
        return res
        


        