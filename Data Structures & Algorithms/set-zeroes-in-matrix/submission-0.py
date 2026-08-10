class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row,col = len(matrix),len(matrix[0])
        A,B = [False]*row,[False]*col
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    A[r] = True
                    B[c] = True
        for r in range(row):
            for c in range(col):
                if A[r] or B[c]:
                    matrix[r][c] = 0


        
        