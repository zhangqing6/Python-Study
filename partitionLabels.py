class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {char: idx for idx, char in enumerate(s)}
        res = []
        start = 0
        end = 0
        
        for i, c in enumerate(s):
            # 更新当前片段最远右边界
            end = max(end, last[c])
            # 走到右边界，分割
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
