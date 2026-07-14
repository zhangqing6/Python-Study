class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)  # 转成集合，查询快 O(1)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # 空字符串合法
        
        for i in range(1, n + 1):
            for j in range(i):  # 遍历 0 ~ i-1
                # 前j个可以拆分 + j~i是字典单词
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # 找到一个就行，不用再找
        
        return dp[n]
