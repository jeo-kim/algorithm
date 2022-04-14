class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        """
               item, next
        5  Node(5, node4)
        4  Node(4, node3)
        3  Node(3, node2)
        2  Node(2, node1)
        1  Node(1, None)
        """

        if self.top is None:
            return None


        topNode = self.top   # (1)
        self.top = self.top.next  # (2) 이 두 가지 순서가 중요하다.

        return topNode.item

    def is_empty(self):
        return self.top is None


class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        # 몇 가지 경우가 있다.
        if not self.front:
            self.front = Node(value, None)
            return

        ## 이미 들어온 값이 있다면 끝까지 가야 한다.
        node = self.front  # 첫 요소로부터
        while node and node.next:  # while node.next 라고 해도 괜찮다고 하셨는데....? aa
            node = node.next  # 언젠가는 node.next가 None이 될 거에요. 끝까지 가서,

        # node가 None이면 next를 붙일 수가 없다.  그래서 aa
        node.next = None(value, None)  # 그 마지막 아이에다가 붙여준다.




    def pop(self):
        """
        (1 --> pop)
        2  <== front
        3
        4
        5
        """
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next

        return node.item

    def is_empty(self):
        return self.front is None



