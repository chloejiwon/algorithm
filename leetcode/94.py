# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
# Solution 1
# Brute Force (Recursion)
# beat 46.12%
class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		if not root:
			return res
		res+=(self.inorderTraversal(root.left))
		res.append(root.val)
		res+=(self.inorderTraversla(root.right))
		return res

