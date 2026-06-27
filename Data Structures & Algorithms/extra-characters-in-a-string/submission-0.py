class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        for w in dictionary:
            self.insert(w)
        memo = {}
        def dfs(i):
            if i == len(s):
                return 0
            if i in memo:
                return memo[i]
            c = 1 + dfs(i+1)
            curr = self.root
            for j in range(i,len(s)):
                char = s[j]
                if char not in curr.children:
                    break
                curr = curr.children[char]
                if curr.isWord:
                    c = min(c,dfs(j+1))
            memo[i] = c
            return c
        return dfs(0)