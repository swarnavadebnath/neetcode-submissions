class Solution:
    def simplifyPath(self, path: str) -> str:
        l=path.split('/')
        s=[]
        for i in l:
            if i=='' or i=='.':
                continue
            elif i=='..':
                if not s:
                    continue
                else:
                    s.pop()
            else:
                s.append("/"+i)
        dir=""
        if not s:
            return "/"
        else:
          for i in s:
            dir+=i
          return dir

        