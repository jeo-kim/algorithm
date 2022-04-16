class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, val):
        self.head = Node(val)

    def append(self, val):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)

    def convertToList(self):
        cur = self.head
        toList = []
        while cur is not None:
            toList.append(cur)
            cur = cur.next
        return toList

    def deleteNodeByIndex(self, index):
        cur = self.head
        cnt = 0

        if index == 0:
            self.head = cur.next
            return

        while cur.next is not None:
            if cnt + 1 == index:
                cur.next = cur.next.next
                return
            else:
                cur = cur.next
                cnt += 1

    def get_node(self, index):
        cur = self.head
        cnt = 0

        while True:
            if cnt == index:
                return cur
            cur = cur.next
            cnt += 1

    def insertNode(self, index, val):
        if index == 0:
            tmp = self.head
            self.head = Node(val)
            self.head.next = tmp
            return

        else:
            prevn = self.get_node(index - 1)
            nextn = self.get_node(index)
            newn = Node(val)
            prevn.next = newn
            newn.next = nextn
            return


list = LinkedList(0)
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
assert len(list.convertToList()) == 6, "원소 개수가 6개가 아닙니다."

list.insertNode(5, 6)
assert list.get_node(5).val == 6, "5번 인덱스의 값이 6이 아닙니다."

list.deleteNodeByIndex(0)
assert list.get_node(0).val == 1, "0번 인덱스 노드 값이 1이 아닙니다."
assert len(list.convertToList()) == 6, "원소 개수가 6개가 아닙니다."

