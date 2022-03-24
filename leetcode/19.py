# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        head2 = head
        while head2:
            head2 = head2.next
            length += 1
        cnt = length-n
        head2, prev = head, None
        while head2:
            if cnt == 0:
                break
            prev = head2
            head2 = head2.next
            cnt -= 1
                
        if not prev:
            return head2.next
        
        prev.next=head2.next
        return head
