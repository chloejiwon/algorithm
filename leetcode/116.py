# 116. Populating Next Right Pointers in Each Node

 Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Solution 1 
# Time Complexity : O(NlogN)
# Using recursion, beat 78.70% 

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def makeNextPointer(node):
                if not node:
                    return
                if node.left:
                    node.left.next = node.right
                if node.right:
                    if node.next :
                        node.right.next = node.next.left
                    else :
                        node.right.next = None
                makeNextPointer(node.left)
                makeNextPointer(node.right)
        makeNextPointer(root)
        return root

# Soltuion Use BFS / DFS
