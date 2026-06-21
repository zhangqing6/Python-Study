class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(i, j, k):
            # 越界 或 字符不匹配
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            # 全部匹配完成
            if k == len(word) - 1:
                return True
            # 标记已访问
            temp = board[i][j]
            board[i][j] = '/'
            # 四个方向递归
            res = False
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if dfs(ni, nj, k + 1):
                    res = True
                    break
            # 回溯恢复
            board[i][j] = temp
            return res

        # 遍历每个起点
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
