class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stck = []
        area = 0
        for i in range(len(heights)):
            while stck and heights[stck[-1]]>heights[i]:
                b = stck.pop()
                width = i - stck[-1] - 1 if stck else i
                area = max(area,heights[b]*width)
            stck.append(i)
        return area

        