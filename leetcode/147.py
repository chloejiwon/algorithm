# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        cur = ListNode(-5001)
        parent = cur
        
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
                
            cur.next, head, cur.next.next = head, head.next, cur.next
            
            if head and cur.val >= head.val:
                cur = parent
        
        return parent.next
