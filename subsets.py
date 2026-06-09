class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        # 回溯函数：path=当前子集，start=遍历起始索引
        def backtrack(path, start):
            # 关键：所有路径都是子集，直接加入结果（包含空集）
            result.append(path[:])
            
            # 从start开始遍历，不回头，避免重复子集
            for i in range(start, len(nums)):
                # 选择：加入当前元素
                path.append(nums[i])
                # 递归：下一次从 i+1 开始选
                backtrack(path, i + 1)
                # 回溯：撤销选择
                path.pop()
        
        # 初始调用：空集，从索引0开始
        backtrack([], 0)
        return result
