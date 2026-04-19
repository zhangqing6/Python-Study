# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        dummy.next=head
        curr=dummy
        while curr.next and curr.next.next:
            first=curr.next
            second= curr.next.next
            first.next=second.next
            second.next=first
            curr.next=second
            curr=first
        return dummy.next
