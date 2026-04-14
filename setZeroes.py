class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        # 记录：第一行、第一列 原来有没有 0
        first_row_zero = False
        first_col_zero = False

        # 1. 检查第一行有没有 0
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # 2. 检查第一列有没有 0
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # 3. 用【第一行+第一列】标记哪些行/列要置0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0   # 第 i 行需要置 0
                    matrix[0][j] = 0   # 第 j 列需要置 0

        # 4. 根据标记，把中间区域置 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 5. 最后处理第一行、第一列
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
