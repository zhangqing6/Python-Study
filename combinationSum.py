class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
    
        def backtrack(start, path, total):
            # 和等于目标，记录答案
            if total == target:
                res.append(list(path))
                return
            # 和超过目标，剪枝
            if total > target:
                return
            # 从start开始，允许重复取当前数字
            for i in range(start, len(candidates)):
                num = candidates[i]
                path.append(num)
                backtrack(i, path, total + num)
                path.pop()  # 回溯撤销
        
        backtrack(0, [], 0)
        return res
