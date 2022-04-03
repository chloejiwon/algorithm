# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = float('-inf')
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(cur: Optional[TreeNode]) -> int:
            if not cur:
                return 0
            if not cur.left and not cur.right:
                self.res = max(self.res, cur.val)	
                return cur.val

            left = right = 0
            if cur.left:
                left = dfs(cur.left)
            if cur.right:
                right = dfs(cur.right)

            self.res = max(self.res, cur.val+max(left,right,0), cur.val+left+right)
            return cur.val+max(left, right, 0)
        
        r = dfs(root.right)
        l = dfs(root.left)
        self.res = max(self.res, root.val+max(l,r,0), root.val+l+r)

        return self.res
