# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # 1. 先把左、右子树分别展开
        self.flatten(root.left)
        self.flatten(root.right)
        
        # 2. 把展开后的左子树挂到右边
        left = root.left
        right = root.right
        
        root.left = None   # 左子树置空
        root.right = left  # 右指针指向原来的左子树
        
        # 3. 找到现在右子树的最后一个节点，把原来的右子树接上去
        temp = root
        while temp.right:
            temp = temp.right
        temp.right = right
