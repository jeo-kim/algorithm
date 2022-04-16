class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def enQueue(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def deQueue(self):
        if self.head is None:
            return -1
        value = self.head.val
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return value

if __name__ == "__main__":
    linkedList = SinglyLinkedList()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    linkedList.enQueue(node1)
    linkedList.enQueue(node2)
    linkedList.enQueue(node3)

    assert linkedList.deQueue() == 1
    assert linkedList.deQueue() == 2
    assert linkedList.deQueue() == 3
