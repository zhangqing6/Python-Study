class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        # dp[i][j] 表示 s[i...j] 是否回文
        dp = [[False] * n for _ in range(n)]
        
        # 预处理回文数组
        for length in range(1, n + 1):  # 子串长度
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
        
        res = []
        path = []
        
        def backtrack(start):
            # 分割到字符串末尾，记录当前方案
            if start == n:
                res.append(list(path))
                return
            # 枚举结束位置
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start:end+1])
                    backtrack(end + 1)
                    path.pop()  # 回溯
        
        backtrack(0)
        return res
