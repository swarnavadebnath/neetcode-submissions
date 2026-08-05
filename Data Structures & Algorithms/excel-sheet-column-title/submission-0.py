class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber>0:
            columnNumber -=1
            offset = columnNumber % 26
            s+= chr(ord('A')+offset)
            columnNumber //= 26
        return s[::-1]
        