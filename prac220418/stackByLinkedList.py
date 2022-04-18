class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class StackByLinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        top = self.head
        self.head = self.head.next
        return top.val

stack = StackByLinkedList()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

