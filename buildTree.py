# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_left, pre_right, in_left, in_right):
            # 递归终止条件：没有节点可以构造
            if pre_left > pre_right:
                return None
            
            # 先序遍历第一个节点就是根节点
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            
            # 找到根节点在中序遍历中的位置
            root_idx = inorder_map[root_val]
            # 左子树的节点个数
            left_size = root_idx - in_left
            
            # 递归构造左子树
            # 先序：根节点后 left_size 个元素 → 左子树
            # 中序：根节点左侧所有元素 → 左子树
            root.left = build(pre_left + 1, pre_left + left_size, in_left, root_idx - 1)
            
            # 递归构造右子树
            # 先序：左子树后剩余元素 → 右子树
            # 中序：根节点右侧所有元素 → 右子树
            root.right = build(pre_left + left_size + 1, pre_right, root_idx + 1, in_right)
            
            return root
        
        # 初始调用：遍历整个数组
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
