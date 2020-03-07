"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def countDepth(self,level,node):
        if not node.children:
            return level
        maxValue = 0
        for child in node.children:
                tmp = self.countDepth(level+1,child)
                if maxValue < tmp:
                        maxValue = tmp
        return maxValue
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
                return 0
        return self.countDepth(1,root)
