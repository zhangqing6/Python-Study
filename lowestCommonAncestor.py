# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node):
            # 空节点 或 找到p/q，直接返回
            if not node or node == p or node == q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            # 左右各找到一个，当前就是公共祖先
            if left and right:
                return node
            # 哪边有结果返回哪边
            return left if left else right
        
        return dfs(root)




