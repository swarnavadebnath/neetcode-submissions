class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        row = defaultdict(set)
        sq = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val==".":
                    continue
                if (val in row[r] or val in cols[c] or val in sq[(r//3,c//3)]):
                    return False
                cols[c].add(val)
                row[r].add(val)
                sq[(r//3,c//3)].add(val)
        return True

        
        