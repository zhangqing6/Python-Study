class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        for i in range(m):
            for j in range(i,m):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(m):
            matrix[i].reverse()
