class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        row = len(grid)
        col = len(grid[0])
        queue = collections.deque()
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    count+=1
        time = 0
        direc = [[-1,0],[1,0],[0,1],[0,-1]]
        while queue and count>0:
            time+=1
            size = len(queue)
            for i in range(size):
                r,c = queue.popleft()
                for dr,dc in direc:
                    nr,nc = r+dr,c+dc
                    if(nr<0 or nr>=row or nc<0 or nc>=col or grid[nr][nc]!=1):
                        continue
                    grid[nr][nc] = 2
                    count-=1
                    queue.append((nr,nc))
        if count>0:
            return -1
        return time


        