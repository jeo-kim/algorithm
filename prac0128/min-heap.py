class MinHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        cur = len(self)
        parent = cur // 2

        while parent > 0:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
            cur = parent
            parent = cur // 2

        #  변형 시도
        # while parent > 0 and self.items[cur] < self.items[parent]:
        #     self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
        #     cur = parent
        #     parent = cur // 2

    def _percolate_down(self, cur):
        # 가장 작은 값이 와야 할 자리를 biggest 라는 변수로 마련해둔다.
        smallest = cur
        left = cur * 2
        right = cur * 2 + 1

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != cur:
            self.items[cur], self.items[smallest] = self.items[smallest], self.items[cur]

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        root = self.items.pop()
        self._percolate_down(1)

        return root

minheap = MinHeap()

# inputs = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]
# inputs = [0, 0, 1, 2, 3, 0, 0, 0]
inputs = []
n = int(input().rstrip())
for _ in range(n):
    inputs.append(int(input().rstrip()))

for input in inputs:
    if input == 0:
        top = minheap.extract()
        if top is None:
            print(0)
        else:
            print(top)

    else:
        minheap.insert(input)