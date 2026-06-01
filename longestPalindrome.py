class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.start = 0
        self.max_len = 1
        
        # 遍历每个字符作为中心
        for i in range(len(s)):
            # 奇数长度回文（中心1个）
            self.expand(s, i, i)
            # 偶数长度回文（中心2个）
            self.expand(s, i, i+1)
        
        # 返回最长回文子串
        return s[self.start : self.start + self.max_len]
    
    # 扩散函数：从 left, right 向两边扩
    def expand(self, s, left, right):
        # 只要左右相等，就一直扩
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # 退出循环时，最后一次有效长度
        cur_len = right - left - 1
        
        # 如果当前更长，更新最大值
        if cur_len > self.max_len:
            self.max_len = cur_len
            self.start = left + 1
