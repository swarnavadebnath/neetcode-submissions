class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        indegree = [[0]*col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                for d in directions:
                    nr,nc = d[0]+r,d[1]+c
                    if (0<=nr<row and 0<=nc<col and matrix[nr][nc]<matrix[r][c]):
                        indegree[r][c] +=1
        q = deque()
        for r in range(row):
            for c in range(col):
                if indegree[r][c] == 0:
                    q.append((r,c))
        l = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for d in directions:
                 nr,nc = r + d[0],c + d[1]
                 if(0<=nr<row and 0<=nc<col and matrix[nr][nc]>matrix[r][c]):
                    indegree[nr][nc] -=1
                    if indegree[nr][nc] == 0:
                        q.append((nr,nc))
            l+=1
        return l                


        