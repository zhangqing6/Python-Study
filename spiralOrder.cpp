class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 定义四个边界：上、下、左、右
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []  # 存储结果
        
        while True:
            # 1. 从左到右遍历上边界
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1  # 上边界向下收缩
            if top > bottom:  # 边界交叉，结束循环
                break
            
            # 2. 从上到下遍历右边界
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1  # 右边界向左收缩
            if left > right:
                break
            
            # 3. 从右到左遍历下边界
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1  # 下边界向上收缩
            if top > bottom:
                break
            
            # 4. 从下到上遍历左边界
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1  # 左边界向右收缩
            if left > right:
                break
        
        return res
