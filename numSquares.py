class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 基准条件：和为0需要0个数
        
        for i in range(1, n + 1):
            # 遍历所有小于等于 i 的完全平方数
            j = 1
            while j * j <= i:
                # 状态转移方程
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[n]
