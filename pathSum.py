# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        # 前缀和哈希表：key=前缀和，value=出现次数
        prefix_map = {0: 1}  # 初始：前缀和0出现1次（处理从根开始的路径）
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            count = 0
            # 更新当前前缀和
            current_sum += node.val
            
            # 核心：若 current_sum - targetSum 存在，说明有路径和为 targetSum
            count += prefix_map.get(current_sum - targetSum, 0)
            
            # 将当前前缀和加入哈希表
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
            
            # 递归左右子树
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # 回溯：移除当前前缀和（避免影响其他路径）
            prefix_map[current_sum] -= 1
            if prefix_map[current_sum] == 0:
                del prefix_map[current_sum]
            
            return count
        
        return dfs(root, 0)
