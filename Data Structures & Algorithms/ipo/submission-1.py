import heapq as hp
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pro = []
        maxheap = []
        for i in range(len(capital)):
            pro.append([capital[i],profits[i]])
        pro.sort()
        i = 0
        j = 0
        while j<k:
            while i<len(pro) and pro[i][0]<=w:
                hp.heappush(maxheap,-pro[i][1])
                i+=1
            if maxheap:
                w-=hp.heappop(maxheap)
            else:
                break
            j+=1
        return w
                
            
            

                

