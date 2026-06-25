class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr = curr.children[c]
        curr.isWord = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        R = len(board)
        C = len(board[0])
        for w in words:
            self.insert(w)
        def dfs(r,c,node,s):
            if r<0 or c<0 or r>=R or c>=C or board[r][c] not in node.children:
                return
            ch = board[r][c]
            curr = node.children[ch]
            s+=ch
            if curr.isWord:
                res.append(s)
                curr.isWord = False
            board[r][c] = "#"
            dfs(r+1,c,curr,s)
            dfs(r-1,c,curr,s)
            dfs(r,c+1,curr,s)
            dfs(r,c-1,curr,s)
            board[r][c] = ch
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,self.root,"")
        return res
        


        