class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        if "0000" in deadends:
            return -1
        visit = set(deadends)
        q = deque(["0000"])
        visit.add("0000")
        steps = 0
        while q:
            steps+=1
            for _ in range(len(q)):
                lock = q.popleft()
                for i in range(4):
                    for j in [1,-1]:
                        digit = str((int(lock[i])+j+10)%10)
                        nextlock = lock[:i] + digit + lock[i+1:]
                        if nextlock in visit:
                            continue
                        if nextlock == target:
                            return steps
                        q.append(nextlock)
                        visit.add(nextlock)
        return -1


        
        