# Definition for singly-linked list.
import collections


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node5 = ListNode(5)
node2 = ListNode(2)
node7 = ListNode(7)
node1 = ListNode(1)
node6 = ListNode(6)
node4 = ListNode(4)
node3 = ListNode(3)

node5.next = node2
node2.next = node7
node7.next = node1
node1.next = node6
node6.next = node4
node4.next = node3

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        que = collections.deque()
        que.append(head)
        to_list = []

        # 연결리스트를 리스트로
        while que:
            node = que.popleft()
            to_list.append(node.val)
            if node.next:
                que.append(node.next)

        print(f"quick sort 전 to_list: {to_list}")

        # quick sort
        def quick_sort(lst, lt, rt):
            if lt < rt:
                i = lt
                pivot = lst[rt]
                for j in range(lt, rt):
                    if lst[j] <= pivot:
                        lst[i], lst[j] = lst[j], lst[i]
                        i += 1
                # 하나의 pivot 에 대해, 비교 대상이 되는 j가 pivot 직전까지 다 돌았다면,
                # 현재 구간을 나누어주던 i 자리에 pivot 이 들어간다. (스왑)
                lst[rt], lst[i] = lst[i], lst[rt]
                quick_sort(lst, lt, i-1)
                quick_sort(lst, i+1, rt)

        quick_sort(to_list, 0, len(to_list)-1)
        print(f"quick sort 후 to_list: {to_list}")

        parent = ListNode(0)
        root = ListNode(to_list[0])
        parent.next = root
        for_converting = collections.deque()
        for_converting.append(root)

        for i in range(1, len(to_list)):
            node = for_converting.popleft()
            node.next = ListNode(to_list[i])
            for_converting.append(node.next)

        return root

        print(f"만들어진 root 값은:{root.val}")
        print(f"만들어진 root.next 값은:{root.next.val}")
        print(f"만들어진 root.next.next 값은:{root.next.next.val}")
        print(f"만들어진 root.next.next.next 값은:{root.next.next.next.val}")
        # print(f"만들어진 root.next 값은:{root.next.val}")

sol = Solution()
print("return 값: ", sol.sortList(node5))
