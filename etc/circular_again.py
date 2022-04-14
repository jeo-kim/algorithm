class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.front = 0
        self.rear = 0
        self.q = [None] * k
        self.max_size = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.q[self.rear] is None:
            # 배열 중에 rear 가 가리키는 인덱스가 None이라면,
            # 아직 비어 있는 것이므로
            self.q[self.rear] = value
            # 그 자리에 지금 넣을 값을 넣어준다.
            if self.rear < self.max_size:
                self.rear = self.rear + 1 # max 인 k보다 작은 인덱스라면
            elif self.rear == self.max_size:
                self.rear = 1  # 다시 출발점으로
            # 이렇게 하면 교재에서의
            # self.rear = (self.rear + 1)

    def deQueue(self):
        """
        :rtype: bool
        """

    def Front(self):
        """
        :rtype: int
        """

    def Rear(self):
        """
        :rtype: int
        """

    def isEmpty(self):
        """
        :rtype: bool
        """

    def isFull(self):
        """
        :rtype: bool
        """

