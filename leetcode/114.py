# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        q = collections.deque()
        
        def dfs_preorder(cur):
            if not cur:
                return
            
            q.append(cur)
            if cur.left:
                dfs_preorder(cur.left)
            if cur.right:
                dfs_preorder(cur.right)
            return
        
        dfs_preorder(root)
        prev = root
        while q:
            node = q.popleft()
            if node == root:
                root.left = None
                root.right = None
                continue
                
            node.left = None
            node.right = None
            
            prev.right = node
            prev = prev.right
