# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        temp = root
        length = 0
        while temp:
            length+=1
            temp = temp.next
        remainder = length % k
        each_size = int(length / k)
        res = []
        temp = root
        for i in range(remainder):
            tmp = ListNode(None)
            tail = tmp
            for j in range(each_size+1):
                curr = ListNode(temp.val)
                tail.next = curr
                tail = tail.next
                temp = temp.next
            res.append(tmp.next)
        for i in range(k-remainder):
            tmp = ListNode(None)
            tail = tmp
            for j in range(each_size):
                curr = ListNode(temp.val)
                tail.next = curr
                tail = tail.next
                temp = temp.next
            res.append(tmp.next)
        return res
        
        
