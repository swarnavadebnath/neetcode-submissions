class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        distance = {}
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
              distance[(i,j)] = float('inf')
        distance[(0,0)] = grid[0][0]
        queue = [(grid[0][0],(0,0))]
        while queue:
            lvl,cord = heapq.heappop(queue)
            r,c = cord
            if lvl > distance[cord]:
                continue
            for dr,dc in dir:
                nr,nc = dr+r,dc+c
                if (nr<0 or nr>=row or nc<0 or nc>=col):
                    continue
                weight = max(grid[r][c],grid[nr][nc])
                time = max(lvl,weight)
                if time<distance[(nr,nc)]:
                    distance[(nr,nc)] = time
                    heapq.heappush(queue,(time,(nr,nc)))
        return distance[(row-1,col-1)]
                

        