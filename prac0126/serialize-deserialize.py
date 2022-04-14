# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3    # deserialize 할 때 편의를 위해서 0번째 인덱스에 추가해두기
node3.left = node4
node3.right = node5

class Codec:

    def serialize(self, root):
        que = collections.deque()
        que.append(root)

        res = ["*"]

        while que:
            node = que.popleft()

            if node:
                res.append(node.val)
                que.append(node.left)
                que.append(node.right)
            else:
                res.append("*")

        return " ".join((list(map(str, res))))


    def deserialize(self, data):
        if data == "* *":
            return None

        modified_data = data.split()
        que = collections.deque()
        root = TreeNode(int(modified_data[1]))
        que.append(root)

        i = 1

        while i*2 + 1 < len(modified_data):
            node = que.popleft()
            if modified_data[i*2] != "*":
                node.left = TreeNode(int(modified_data[i*2]))
                que.append(node.left)
            else:
                node.left = None

            if modified_data[i*2+1] != "*":
                node.right = TreeNode(int(modified_data[i*2+1]))
                que.append(node.right)
            else:
                node.right = None

            i += 1

        return root





codec = Codec()
print(codec.serialize(node1))

codec.deserialize(codec.serialize(node1))