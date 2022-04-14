# Definition for singly-linked list.
import collections

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node4 = ListNode(4)
node2 = ListNode(2)
node1 = ListNode(1)
node3 = ListNode(3)

node4.next = node2
node2.next = node1
node1.next = node3

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 예외 처리
        if head.next is None:
            return head

         #  연결리스트인 채로 다룰 자신이 없어서 리스트로 바꿔서 해보기
        to_list = []
        que = collections.deque()
        que.append(head)

        while que:
            node = que.popleft()
            to_list.append(node.val)
            if node.next:
                que.append(node.next)

        print(f"정렬 전 {to_list}")

        for cur in range(1, len(to_list)):
            for delta in range(1, cur + 1):
                cmp = cur - delta
                if to_list[cmp] > to_list[cmp + 1]:
                    to_list[cmp], to_list[cmp + 1] = to_list[cmp + 1], to_list[cmp]
                else:
                    break

        print(f"정렬 후 {to_list}")

        # 노드들의 연결 관계로 다시 바꿔 주기

        # 대기 노드 큐
        result_que = collections.deque()
        root_node = ListNode(to_list[0])
        result_que.append(root_node)

        # 완성 노드 큐
        result_2_que = collections.deque()

        for i in range(1, len(to_list)):
            node_1 = result_que.popleft()
            node_2 = ListNode(to_list[i])
            node_1.next = node_2
            result_que.append(node_2)
            result_2_que.append(node_1)

        root = result_2_que.popleft()

        return root

sol = Solution()
sol.insertionSortList(node4)


def insertionSortList(head: ListNode) -> ListNode:
    cur = parent = ListNode(0)

#
# while head:
#     while cur.next and cur.next.val < head.val:
#         cur = cur.next
#
#     cur.next, head.next, head = head, cur.next, head.next
#
#     if head and cur.val > head.val:
#         cur = parent
#
# return parent.next


