class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class QueByLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def popleft(self):
        if self.head is None:
            return None
        else:
            res = self.head.val
            self.head = self.head.next
            return res

que = QueByLinkedList()
que.push(1)
que.push(2)
que.push(3)
que.push(4)

assert que.popleft() == 1
assert que.popleft() == 2
assert que.popleft() == 3
assert que.popleft() == 4
assert que.popleft() is None, "None이 아님!"
