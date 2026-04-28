# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(node, low, high):
            # 空树合法
            if not node:
                return True
            
            # 当前节点值必须大于下界，小于上界
            if node.val <= low or node.val >= high:
                return False
            
            # 左子树：上界变成当前节点值
            left_ok = helper(node.left, low, node.val)
            # 右子树：下界变成当前节点值
            right_ok = helper(node.right, node.val, high)
            
            return left_ok and right_ok
        
        # 初始：根节点范围 (-无穷, +无穷)
        return helper(root, float('-inf'), float('inf'))
