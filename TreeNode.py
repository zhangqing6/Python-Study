# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(node, level):
            if not node:
                return
            # 新层级，创建空列表
            if len(res) == level:
                res.append([])
            # 对应层级添加值
            res[level].append(node.val)
            # 递归左右子树
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return res
