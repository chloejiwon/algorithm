# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
# Solution 1
# Brute Force (Recursion)
# Time Complexity O(n) (because, T(n) = 2*T(n/2)+1)
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
# Solution 2
# Using Stack! (with tree pointer)
# Need to DO One more time ON MY OWN!!
# Time Complexity : O(n)
class Solution(object):
        def inorderTraversal(self, root):
                """
                :type root: TreeNode
                :rtype: List[int]
                """
		# 1. Push root and root.left ....
		# 2. after pushing all left nodes, pop one and append
		# 3. Make node.right is root again and Do the same(back to #1)
		res,stack = [],[]
		while True:
			while root:
				stack.append(root)
				root = root.left
			if not stack:
				return res
			node = stack.pop()
			res.append(node)
			root = node.right
