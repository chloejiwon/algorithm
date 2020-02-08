# 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
# Solution 1
def maxDepth(root):
	"""
	: type root : TreeNode
	: rtype : int
	"""
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

# Solution 2
def maxDepth(root):
	self.maxDepth = 0
	def dfs(root,depth):
		if not root: return
		if not root.left and not root.right:
			self.maxDepth = 
