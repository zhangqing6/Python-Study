class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        
        # 定义双向链表节点结构
        class Node:
            def __init__(self, k=0, v=0):
                self.key = k
                self.val = v
                self.prev = None
                self.next = None
        
        self.Node = Node
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)
        else:
            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self.addToHead(new_node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                del self.cache[removed.key]
                self.size -= 1

    # 添加到头部
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # 删除节点
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 移到头部
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    # 删除尾部
    def removeTail(self):
        res = self.tail.prev
        self.removeNode(res)
        return res
