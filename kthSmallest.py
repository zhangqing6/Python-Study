# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        stack = []
        current = root
        
        while stack or current:
            # 一直遍历到最左节点
            while current:
                stack.append(current)
                current = current.left
            
            # 弹出节点（当前最小节点）
            current = stack.pop()
            k -= 1
            # 找到第k小元素，直接返回
            if k == 0:
                return current.val
            
            # 遍历右子树
            current = current.right
