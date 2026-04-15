class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        count=0
        m=len(matrix)
        n=len(matrix[0])
        row=m-1
        col=0
        while row>=0 and col<n:
            current=matrix[row][col]
            if current==target:
                return True
            if current>target:
                row-=1
            if current<target:
                col+=1

        return False
