class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ===================== 前序遍历 =====================
# 递归
def preorder_recur(root):
    res = []
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res

# 迭代
def preorder_iter(root):
    res = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        cur = cur.right
    return res


# ===================== 中序遍历 =====================
# 递归
def inorder_recur(root):
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)
    dfs(root)
    return res

# 迭代
def inorder_iter(root):
    res = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res


# ===================== 后序遍历 =====================
# 递归
def postorder_recur(root):
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)
    dfs(root)
    return res

# 迭代（最好记的版本：前序翻转）
def postorder_iter(root):
    res = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            res.append(cur.val)
            stack.append(cur)
            cur = cur.right   # 这里先右
        cur = stack.pop()
        cur = cur.left        # 再左
    return res[::-1]  # 最后反转


# ===================== 测试 =====================
if __name__ == '__main__':
    # 构造树
    #        4
    #      /   \
    #     2     6
    #    / \   /
    #   1  3  5

    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n2 = TreeNode(2, n1, n3)
    n5 = TreeNode(5)
    n6 = TreeNode(6, n5)
    root = TreeNode(4, n2, n6)

    print("前序 递归:", preorder_recur(root))
    print("前序 迭代:", preorder_iter(root))
    print("中序 递归:", inorder_recur(root))
    print("中序 迭代:", inorder_iter(root))
    print("后序 递归:", postorder_recur(root))
    print("后序 迭代:", postorder_iter(root))
