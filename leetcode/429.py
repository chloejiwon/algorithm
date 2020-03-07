# 429.py N-ary Tree Level Order Traversal
# Definition for a Node.
import Queue
class Node(object):
	def __init__(self, val=None, children=None):
		self.val = val
		self.children = children
import Queue
class Solution(object):
        def levelOrder(self,root):
                """
                :type root: Node
                :rtype: List[List[int]]
                """
                res = []
                if not root:
                        return res
                q = Queue.Queue()
                q.put(root)
                while q.empty()==False:
                        # put root's children
                        tmp = []
                        size = q.qsize()
                        for i in range(size):
                            cur = q.get()
                            tmp.append(cur.val)
                            for child in cur.children:
                                q.put(child)
                        res.append(tmp)
                return res 

