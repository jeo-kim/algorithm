# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    longest = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node: TreeNode):
            if not node:
                return -1


            # 왼쪽 오른쪽 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)

            # 아들 노드에 1을 더해서 상태값 리턴
            return max(left, right) + 1

        dfs(root)
        return self.longest
