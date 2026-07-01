class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks)%4 != 0:
            return False
        sides = [0,0,0,0]
        target = sum(matchsticks)//4
        matchsticks.sort(reverse=True)
        def dfs(i):
            nonlocal sides
            if i>=len(matchsticks):
                return True
            for j in range(4):
                if matchsticks[i]+ sides[j]>target:
                    continue
                if j>0 and sides[j]==sides[j-1]:
                    continue
                sides[j]+=matchsticks[i]
                if dfs(i+1):
                    return True
                sides[j]-=matchsticks[i]
            return False
        return dfs(0)


        