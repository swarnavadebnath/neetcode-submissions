class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        nodes = set(''.join(words))
        visit = set()
        n = len(nodes)
        degree = {}
        for s in nodes:
            degree[s] = 0
        adj = defaultdict(list)
        for i in range(0,len(words)-1):
            a = words[i]
            b = words[i+1]
            c = 0
            for j in range(min(len(a),len(b))):
                if a[j] != b[j]:
                    c+=1
                    if (a[j],b[j]) not in visit:
                        adj[a[j]].append(b[j])
                        degree[b[j]]+=1
                        visit.add((a[j],b[j]))
                    break
            if c == 0 and len(b)<len(a):
                return ""
                    
        queue = deque()
        res = ""
        for s in nodes:
            if degree[s] == 0:
                queue.append(s)
        while queue:
            cur = queue.popleft()
            res = res + cur
            for p in adj[cur]:
                degree[p] -= 1
                if degree[p] == 0:
                    queue.append(p)
        if len(res) < n:
            return ""
        return res



        
        