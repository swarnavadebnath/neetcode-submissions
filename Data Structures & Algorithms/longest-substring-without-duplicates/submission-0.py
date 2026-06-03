class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        window=set()
        longest=0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            siz=(r-l)+1
            longest=max(longest,siz)
            window.add(s[r])
        return longest



        