# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_diameter = 0
        
        def depth(node):
            # 空节点深度为0
            if not node:
                return 0
            
            # 递归计算左、右子树深度
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # 更新最大直径：当前节点的直径 = 左深度 + 右深度
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            # 返回当前节点的深度：max(左,右) + 1
            return max(left_depth, right_depth) + 1
         # 调用递归函数
        depth(root)
        return self.max_diameter
       
