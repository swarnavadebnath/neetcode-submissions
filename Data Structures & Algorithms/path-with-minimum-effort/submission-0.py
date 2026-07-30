class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        row = len(heights)
        col = len(heights[0])
        visit = set()
        queue = [[0,0,0]]
        while queue:
            diff,r,c = heapq.heappop(queue)
            if (r,c) == (row-1,col-1):
                return diff
            if (r,c) in visit:
                continue
            visit.add((r,c))
            for dr,dc in dir:
                nr,nc = r+dr,c+dc
                if (nr<0 or nr>=row or nc<0 or nc>=col or (nr,nc) in visit):
                    continue
                newdiff = max(diff,abs(heights[r][c]-heights[nr][nc]))
                heapq.heappush(queue,[newdiff,nr,nc])
        return 0



        
        