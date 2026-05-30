class Solution:
    def validPalindrome(self, s: str) -> bool:
        s2=""
        for i in range(len(s)):
            if s[i].isalnum()==False:
                continue
            if i==len(s):
                s2=s[:i]
            else:
                s2=s[:i]+s[i+1:]
            if self.isPalindrome(s2)==True:
                return True
        return False

    def isPalindrome(self,s):
     start=0
     end=len(s)-1
     s=s.lower()
     while start<end:
        if s[start].isalnum()==False:
            start+=1
            continue
        if s[end].isalnum()==False:
            end-=1
            continue
        if s[start]!=s[end]:
            return False
        start+=1
        end-=1
     return True
    



            
        