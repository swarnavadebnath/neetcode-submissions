class Solution:
    def checkValidString(self, s: str) -> bool:
        maxopen = 0
        minopen = 0
        for c in s:
            if c == '(':
                maxopen+=1
                minopen+=1
            elif c == ')':
                maxopen-=1
                minopen-=1
            else:
                maxopen+=1
                minopen-=1
            if maxopen<0:
                return False
            if minopen<0:
                minopen = 0
        return minopen == 0
            
        
        