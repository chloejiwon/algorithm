# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque()
        q.append(root)
        
        res = []
        while q:
            temp = []
            n = len(q)
            for i in range(n):
                cur = q.pop()
                temp.append(cur.val)
                if cur.left:
                    q.appendleft(cur.left)
                if cur.right:
                    q.appendleft(cur.right)
            if temp:
                res.insert(0, temp)
            
        return res
                
