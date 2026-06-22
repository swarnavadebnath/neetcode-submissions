import heapq as hp
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = {'a':a,'b':b,'c':c}
        res = []
        maxheap = [[-c,v] for v,c in d.items() if c>0]
        hp.heapify(maxheap)
        while maxheap:
            val = hp.heappop(maxheap)
            if len(res)>=2 and val[1] == res[-1] and val[1]==res[-2]:
                if maxheap:
                 val2 = hp.heappop(maxheap)
                 val2[0]+=1
                 res.append(val2[1])
                 hp.heappush(maxheap,val)
                 if val2[0]<0:
                    hp.heappush(maxheap,val2)
                else:
                    break
            else:
                val[0]+=1
                res.append(val[1])
                if val[0]<0:
                 hp.heappush(maxheap,val)
        return "".join(res)
    

            

        
        