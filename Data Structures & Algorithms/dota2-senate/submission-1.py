class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        cnt = 0
        i = 0
        senate = list(senate)
        while i<len(senate):
            c = senate[i]
            if c == 'R':
                if cnt<0:
                    senate.append('D')
                cnt+=1
            else:
                if cnt>0:
                    senate.append('R')
                cnt-=1
            i+=1
        if cnt>0:
            return "Radiant"
        else:
            return "Dire"
            



        