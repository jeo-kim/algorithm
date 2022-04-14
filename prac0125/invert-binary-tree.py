# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def invertTree(self, root):

        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def DFS(node):
            if not node:
                return

            else:
                node.left, node.right = node.left, node.right
                DFS(node.left)
                DFS(node.right)

        DFS(root)
        return root