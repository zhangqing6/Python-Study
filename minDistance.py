class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 保证 word2 更短，节省空间
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        n = len(word2)
        dp = list(range(n + 1))
        
        for i in range(1, len(word1) + 1):
            prev = dp[0]
            dp[0] = i
            for j in range(1, n + 1):
                tmp = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = prev
                else:
                    dp[j] = min(prev, dp[j], dp[j-1]) + 1
                prev = tmp
        return dp[-1]
