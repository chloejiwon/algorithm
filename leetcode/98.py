# 98. Validate Binary Search Tree
# Given a binary tree, determine if it is a valid binary search tree(BST).
"""
. The left subtree of a node contains only nodes with keys less than the node's key.
. The right subtree of a node contains only nodes with keys greater than the node's key.
. Both the left and right subtrees must also be binary search trees.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1 
# - Wrong answer
# - understand BST definition fully!
def isValidBST(root):
	"""
	:type root: TreeNode
	:rtype:bool
	"""
        if not root:
            return True
        if root.left!=None and root.left.val >= root.val:
            return False
        if root.right!=None and root.right.val <= root.val:
            return False
        
        return self.isValidBST(root.left) & self.isValidBST(root.right)

# Solution 2
# - Wrong answer
# - Got an idea, but needs clarification
# - idea : keep Max and min value to check values.
def isValidBST(root):
        if not root:
            return True
        
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        
        if root.left :
            self.leftSubMax = root.left.val
        if root.right:
            self.rightSubMin = root.right.val
        
        def findMaxMin(self,node,isLeft):
            #print "===",self.leftSubMax, self.rightSubMin
            if isLeft:
                if node.left and node.left.val > node.val:
                    return False
                if node.right :
                    if node.right.val < node.val:
                        return False
                    if self.leftSubMax < node.right.val:
                        self.leftSubMax = node.right.val
                    findMaxMin(self,node.right,False)
            else:
                if node.right and node.right.val < node.val:
                    return False
                if node.left:
                    if node.left.val > node.val:
                        return False
                    if self.rightSubMin > node.left.val :
                        self.rightSubMin = node.left.val
                    findMaxMin(self,node.left,True)
        if root.left :
            if findMaxMin(self,root.left,True) == False:
                return False
            if self.leftSubMax >= root.val:
                return False
        if root.right:
            if findMaxMin(self,root.right,False) == False:
                return False
            if self.rightSubMin <= root.val:
                return False
        return True

# Solution 3
# - keep solution2 ' s idea but simplify it.
# - solution based
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compareValue(node,maxval = float('inf'),minval=float('-inf')):
            if not node:
                return True

            if node.val <= minval or node.val >= maxval:
                return False
            
            return compareValue(node.left,node.val,minval) & compareValue(node.right,maxval,node.val)
            
        return compareValue(root)
