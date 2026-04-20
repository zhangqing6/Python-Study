# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        dummy.next=head
        curr=dummy
        while True:
            start=curr.next
            end=curr
            for _ in range(k):
                end=end.next
                if not end:
                    return dummy.next
            next_node=end.next
            end.next=None
            prev=None
            cur=start
            while cur:
                next_Node=cur.next
                cur.next=prev
                prev=cur
                cur=next_Node
            curr.next=prev
            start.next=next_node
            curr=start

   
