class BinaryMaxHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        cur = len(self)
        parent = cur // 2

        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            cur = parent
            parent = cur // 2

        #      # todo 질문 하기 - while 문에서 cur 이 if 검사에 걸리지 않아도 while 이 계속 진행되어야 하는지
        #     # while 시작할 때 cur 로 들어온 친구가 바로 만난 자신의 부모보다 크지 않아서
        #     # 위의 if 문을 실행하지 않았어도,
        #     # cur 이라는 pointer 는 위로 올라가면서 검사를 쭉 하는 걸까?
        #     # 꼭 그래야 하는걸까?

        # 이렇게 바꿔보면 어떨까?
        while parent > 0 and self.items[cur] > self.items[parent]:
            self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        # todo 질문 하기 - swap 하지 않고 pop() 하면 안 되지 않을까 궁금 (해결)
        # 스왑을 해야 하지 않나..?
        # 아, 리턴하는 것은 pop 한 값이 아니라 root 이기 때문에 문제가 안 되는 구나.
        self.items[1] = self.items[-1]
        # self.items[1], self.items[-1] = self.items[-1], self.items[1]
        self.items.pop()
        self._percolate_down(1)

        return root

########### 테스트 함수
def test_maxheap_we_made(lst, k):
    maxheap = BinaryMaxHeap()

    for elem in lst:
        maxheap.insert(elem)

    return [maxheap.extract() for _ in range(k)][k - 1]

assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1
