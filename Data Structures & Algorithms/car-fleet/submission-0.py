class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        l=[]
        s=[]
        for i in range(len(pos)):
            l.append((pos[i],speed[i]))
        l.sort(reverse=True)
        for i in l:
            t=(target-i[0])/i[1]
            if not s:
                s.append(t)
            if t<=s[-1]:
                continue
            else:
                s.append(t)
        return len(s)

        