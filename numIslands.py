class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        # 遍历每个格子
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    # 用 DFS 把这块陆地“淹掉”（标记为 0）
                    self.dfs(grid, i, j, m, n)
        
        return count
    
    def dfs(self, grid, i, j, m, n):
        # 越界或不是陆地，直接返回
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return
        
        # 标记为水（避免重复访问）
        grid[i][j] = '0'
        
        # 递归访问上下左右四个方向
        self.dfs(grid, i - 1, j, m, n)  # 上
        self.dfs(grid, i + 1, j, m, n)  # 下
        self.dfs(grid, i, j - 1, m, n)  # 左
        self.dfs(grid, i, j + 1, m, n)  # 右
