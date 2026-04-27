# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        
        # 取数组中间元素作为根节点（保证平衡）
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        # 递归构建左子树（左半部分）
        root.left = self.sortedArrayToBST(nums[:mid])
        # 递归构建右子树（右半部分）
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
