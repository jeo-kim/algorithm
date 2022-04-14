# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections
class Solution(object):


    def mergeTrees(self, root1: TreeNode, root2: TreeNode):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        que = collections.deque(root1, root2)
        while que:
            tmp1 = que.popleft()
            tmp2 = que.popleft()
            
            tmp1.left.val + tmp2.left.val

