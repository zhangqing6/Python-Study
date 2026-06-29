class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        # path保存每行皇后所在列下标
        path = []
        cols = set()       # 占用列
        diag1 = set()      # 行-列
        diag2 = set()      # 行+列

        def backtrack(row):
            if row == n:
                # 格式化棋盘
                board = []
                for col in path:
                    line = ["."] * n
                    line[col] = "Q"
                    board.append("".join(line))
                res.append(board)
                return
            # 枚举当前行每一列
            for col in range(n):
                d1 = row - col
                d2 = row + col
                if col not in cols and d1 not in diag1 and d2 not in diag2:
                    # 放置皇后
                    path.append(col)
                    cols.add(col)
                    diag1.add(d1)
                    diag2.add(d2)
                    backtrack(row + 1)
                    # 回溯撤销
                    path.pop()
                    cols.remove(col)
                    diag1.remove(d1)
                    diag2.remove(d2)

        backtrack(0)
        return res
