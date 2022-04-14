class Solution(object):
    def isBalanced(self, root):
        def DFS(root):
            if not root:
                return 0

            left = DFS(root.left)
            right = DFS(root.right)

            # 균형이 깨졌음을 알려줄 수 있는 세 가지 지표
            if abs(left-right) > 1 or left == -1 or right == -1:
                return -1

            return max(left, right) + 1

        return DFS(root) != -1


