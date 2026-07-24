class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return
        row = len(heights)
        col = len(heights[0])
        pac = set()
        atl = set()
        def dfs(r,c,vis,prev):
            if (r<0 or r>=row or c<0 or c>=col or (r,c) in vis or heights[r][c]<prev):
                return
            vis.add((r,c))
            dfs(r+1,c,vis,heights[r][c])
            dfs(r-1,c,vis,heights[r][c])
            dfs(r,c+1,vis,heights[r][c])
            dfs(r,c-1,vis,heights[r][c])
        for c in range(col):
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,atl,heights[row-1][c])
        for r in range(row):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col-1,atl,heights[r][col-1])
        res = []
        for r in range(row):
            for c in range(col):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res
        
        