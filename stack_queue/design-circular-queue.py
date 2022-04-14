from collections import deque


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.que = deque()  # deque 선언
        self.max_size = k  # 최댓값

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.que.append(value)
            return True
        else:
            return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.que.popleft()
            return True


    def Front(self):
        """
        :rtype: int
        """
        if len(self.que) != 0:
            return self.que[0]
        else:
            return -1

    def Rear(self):
        """
        :rtype: int
        """
        if len(self.que) != 0:
            return self.que[-1]
        else:
            return -1


    def isEmpty(self):
        """
        :rtype: bool
        """
        if len(self.que) == 0:
            return True
        else:
            return False


    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.que) == self.max_size:
            return True
        else:
            False