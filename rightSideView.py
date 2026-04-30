# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])  # 初始化队列
        
        while queue:
            level_size = len(queue)  # 当前层的节点数量
            
            # 遍历当前层的所有节点
            for i in range(level_size):
                node = queue.popleft()
                
                # 只把【每层最后一个节点】加入结果
                if i == level_size - 1:
                    result.append(node.val)
                
                # 把左右子节点加入队列（先左后右）
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
