class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sub = []
        def isPali(s,l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        def dfs(i,j):
            if i>=len(s):
                res.append(sub.copy())
                return
            if j>=len(s):
                return
            dfs(i,j+1)
            if isPali(s,i,j):
                sub.append(s[i:j+1])
                dfs(j+1,j+1)
                sub.pop()
        
        dfs(0,0)
        return res
        
            
        

        