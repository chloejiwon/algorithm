# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate(start: int, end: int) -> []:
            if end < start:
                return [None]
            else:
                res = []
                for k in range(start, end+1):
                    left = generate(start, k-1)
                    right = generate(k+1, end)
                    for l in left:
                        for r in right:
                            root = TreeNode(k)
                            root.left = l
                            root.right = r
                            res.append(root)
                return res
        
        return generate(1, n)
