class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        max_area=0
        heights=[0]+heights+[0]
        n=len(heights)
        for i in range (n):
            while stack and heights[i]<heights[stack[-1]]:
                h_idx = stack.pop()
                height = heights[h_idx]
                
                # 计算宽度：右边界 - 左边界 - 1
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
