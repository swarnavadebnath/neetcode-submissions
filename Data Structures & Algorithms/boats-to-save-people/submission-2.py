class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        c=[]
        while l<=r:
            v=people[l]+people[r]
            if v<=limit:
                c.append([people[l],people[r]])
                l+=1
                r-=1
            else:
                c.append(people[r])
                r-=1
        return len(c)

        