# 2. Add Two Numbers
# Solution 1 - Brute Force
# Make an integer out of two linked list. add them. and make them into linkedlist
# Pass - 84ms, faster than 9.01% 
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
	a,b,i=0,0,0
	while l1 != None:
		for j in range(i):
			l1.val *= 10
		i+=1
		a+=(l1.val)
		l1 = l1.next
	i = 0
	while l2 != None:
		for j in range(i):
			l2.val *= 10
		i+=1
		b+=(l2.val)
		l2 = l2.next
	print a,b,a+b
	a = a+b
	# Make a into List Node res
	res = ListNode(0)
	tail = res
	while True:
		tail.next = ListNode(a%10)
		a = a//10
		if a==0:
			break
		tail = tail.next
	return res.next

# Solution 2 
# Pass - beat 62.78% . But wrong answer few times.. need to be careful 
# Use Carry integer value to make it faster. one loop only
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a,b,carry = 0,0,0
        res = ListNode(0)
        tail = res
        while True:
            if not l1:
                a = 0 
            else : 
                a = l1.val
            if not l2:
                b = 0
            else : 
                b = l2.val

            c = (a+b+carry)%10
            carry = (a+b+carry)//10
            
            tmp = ListNode(c)
            
            tail.next = tmp
            tail = tail.next
            if l1 :
                l1 = l1.next
            if l2:
                l2 = l2.next
            if not l1 and not l2 and carry==0:
                break
        return res.next
            
