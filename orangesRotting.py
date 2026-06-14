class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]  # 上下左右
        
        # 初始化：统计新鲜橘子、存入腐烂橘子坐标
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        time = 0
        # BFS 逐层腐烂
        while q and fresh > 0:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    # 边界合法且是新鲜橘子
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
            time += 1
        
        return time if fresh == 0 else -1
