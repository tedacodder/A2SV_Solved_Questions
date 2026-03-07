# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head1=ListNode()
        head1.next=head
        dummy=head1
        while dummy:
            if dummy.next and dummy.next.val==val: 
                dummy.next=dummy.next.next
            else:
                dummy=dummy.next
        return head1.next
       