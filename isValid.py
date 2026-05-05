class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :type: bool
        """
        # 字典：右括号 → 对应的左括号
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            # 如果是右括号
            if char in mapping:
                # 栈顶元素（如果栈空，用一个无效值）
                top = stack.pop() if stack else '#'
                
                # 不匹配直接返回 False
                if mapping[char] != top:
                    return False
            
            # 如果是左括号，入栈
            else:
                stack.append(char)
        
        # 最后栈必须为空，才算完全匹配
        return len(stack) == 0
