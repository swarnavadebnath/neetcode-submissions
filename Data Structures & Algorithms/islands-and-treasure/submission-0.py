class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        rows = len(grid)
        col = len(grid[0])
        queue = collections.deque()
        visit = set()
        for r in range(rows):
            for c in range(col):
                if grid[r][c] == 0:
                 queue.append((r,c))
                 visit.add((r,c))
        dir = [[1,0],[-1,0],[0,1],[0,-1]]
        dist = 0
        while queue:
            size = len(queue)
            for i in range(size):
                r,c = queue.popleft()
                grid[r][c] = dist
                for dr,dc in dir:
                    nr,nc = r+dr,c+dc
                    if(nr<0 or nr>=rows or nc<0 or nc>=col or grid[nr][nc]==-1 or (nr,nc) in visit):
                        continue
                    queue.append((nr,nc))
                    visit.add((nr,nc))
            dist+=1    

        