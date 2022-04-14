# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    longest = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def DFS(node):
            if not node:
                return 0

            left = DFS(node.left)
            right = DFS(node.right)


            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0

            if left != 0 and right != 0:
                self.longest = max(self.longest, left + right + 2)
            else:
                self.longest = max(self.longest, left, right)

            return max(left, right)

        DFS(root)
        return self.longest



