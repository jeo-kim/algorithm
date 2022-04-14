import collections

class MyQueue(object):

    def __init__(self):
        self.stack1 = collections.deque()
        self.stack2 = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        if len(self.stack2) != 0:
            while len(self.stack2) != 0:
                self.stack1.append()
            return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        if len(self.stack2) != 0:
            peeked = self.stack2.pop()
            self.push(peeked)
            return peeked

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False