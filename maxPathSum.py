# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float("-inf")
        
        def max_gain(node):
            if not node:
                return 0
            # 左右支路负数则舍弃
            left = max(max_gain(node.left), 0)
            right = max(max_gain(node.right), 0)
            # 当前节点作为路径最高点，左右连通的路径和
            current_path = node.val + left + right
            if current_path > self.max_sum:
                self.max_sum = current_path
            # 返回单侧最大分支给父节点
            return node.val + max(left, right)
        
        max_gain(root)
        return self.max_sum
