# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def visitTree(target: int, root: TreeNode) -> []:
            if not root:
                return None
            
            if not root.left and not root.right and target == root.val:
                return [[root.val]]

            paths = []
            
            if root.left:
                left = visitTree(target-root.val, root.left)
                for l in left:
                    k = [root.val]
                    k.extend(l)
                    paths.append(k)
            if root.right:
                right = visitTree(target-root.val, root.right)
                for r in right:
                    k = [root.val]
                    k.extend(r)
                    paths.append(k)
            return paths
            
        return visitTree(targetSum, root)
