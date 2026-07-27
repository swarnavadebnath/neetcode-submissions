class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord==endWord):
            return 0
        wordList.append(beginWord)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*"+word[i+1:]
                adj[pattern].append(word)
        queue = deque()
        queue.append((beginWord,1))
        visit = set([beginWord])
        while queue:
            currentWord,steps = queue.popleft()
            if currentWord == endWord:
                return steps
            for i in range(len(currentWord)):
                pattern = currentWord[:i] + "*" + currentWord[i+1:]
                for w in adj[pattern]:
                    if w not in visit:
                        visit.add(w)
                        queue.append((w,steps+1))
        if not queue:
                return 0
        