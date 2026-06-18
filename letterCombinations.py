class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        # 数字按键映射
        phone = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }
        res = []
        
        def backtrack(index, path):
            # 所有数字匹配完成，存入结果
            if index == len(digits):
                res.append(path)
                return
            # 当前数字对应的字母列表
            chars = phone[digits[index]]
            for c in chars:
                backtrack(index + 1, path + c)
        
        backtrack(0, "")
        return res

