"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        hashmap={}
        cur=head
        while cur:
            hashmap[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            hashmap[cur].next=hashmap.get(cur.next)
            hashmap[cur].random=hashmap.get(cur.random)
            cur=cur.next
        return hashmap.get(head)
