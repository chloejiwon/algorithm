# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        # preorder is root -> left -> right
        if t : 
            ans = ""
            ans += str(t.val)
            if t.left :
                ans += "("
                ans += self.tree2str(t.left)
                ans += ")"
            if t.left == None and t.right :
                ans+= "()"
            if t.right : 
                ans += "("
                ans += self.tree2str(t.right)
                ans += ")"
            return ans
        else :
            return ""
