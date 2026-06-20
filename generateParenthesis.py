class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
    
        def backtrack(path, left, right):
            # 左右括号都凑齐n个，记录结果
            if left == n and right == n:
                res.append(''.join(path))
                return
            # 可以加左括号
            if left < n:
                path.append('(')
                backtrack(path, left + 1, right)
                path.pop()
            # 右括号少于左括号时才能加右括号
            if right < left:
                path.append(')')
                backtrack(path, left, right + 1)
                path.pop()
        
        backtrack([], 0, 0)
        return res
