import heapq as hp
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        minheap = []
        res = []
        i = 0
        time = tasks[0][0]
        while len(res)<len(tasks):
            while i<len(tasks) and tasks[i][0]<=time:
                hp.heappush(minheap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not minheap:
                time = tasks[i][0]
            else:
                val = hp.heappop(minheap)
                res.append(val[1])
                time+=val[0]
        return res
        