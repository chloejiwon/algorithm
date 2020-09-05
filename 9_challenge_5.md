# All Elements in Two Binary Search Trees

## Solution 1 - 22.33%

뭐지 이 처참한 퍼센트는 ? 하지만 그럴 법한 풀이.. 그래도 한번에 accepted 되어 만족.

1. 각 tree를 traverse하면서 list로 만든다 (내가 사용한건  preorder인데 이게 영향을 미쳐?)
1. 리스트를 합쳐서 sort한다

### TimeComplexity : O(The number of Nodes in root1 + The number of Nodes in root 2)

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverseTree(self, root, res):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return res
        res.append(root.val)
        if root.left == None and root.right == None:
            return res
        left = []
        right = []
        if root.left != None:
            left = self.traverseTree(root.left, left)
        if root.right != None:
            right = self.traverseTree(root.right, right)
        return res + left + right 
    
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        res1 = [] 
        res2 = []
        res1 = self.traverseTree(root1, res1)
        res2 = self.traverseTree(root2, res2)
        return sorted(res1 + res2)
```


## Solution 2 - 72.92%

아이디어는 똑같고, 좀 더 이쁘게 다듬어 보았다. 근데 퍼센트 차이...

아마 내가 parameter로 넘기고 하면서 복사, 메모리 참조 등등이 일어나고 이게 엄청 많이 잡아먹는 모양이다. (?)

inorder, preorder 등 traverse하는 방법은 속도에 별 영향을 안 미치는 것 같다. (당연하지..)

### TimeComplexity : O(The number of Nodes in root1 + The number of Nodes in root 2)

```python
class Solution(object):
    def traverseTree(self, root, res):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        res.append(root.val)
        self.traverseTree(root.left, res)
        self.traverseTree(root.right, res)
    
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        res1 = [] 
        res2 = []
        self.traverseTree(root1, res1)
        self.traverseTree(root2, res2)
        return sorted(res1 + res2)

```