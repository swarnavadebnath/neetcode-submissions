import heapq as hp
class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        res = []
        prev = None
        for w in s:
            d[w] = 1 + d.get(w,0)
        maxheap = [[-count, char] for char, count in d.items()]
        hp.heapify(maxheap)
        while maxheap:
            val = hp.heappop(maxheap)
            val[0]+=1
            res.append(val[1])
            if prev:
                hp.heappush(maxheap,prev)
            if val[0]<0:
                prev = val
            else:
                prev = None            
        if prev:
            return ""
        else:
            return "".join(res)
        
        
        

            

        
        