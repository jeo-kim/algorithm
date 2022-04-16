class maxHeap:
    def __init__(self):
        # dummy 1개
        self.que = [0]

    def getParentIndex(self, index):
        return index // 2

    def getLeftChildIndex(self, index):
        return index * 2

    def getRightChildIndex(self, index):
        return index * 2 + 1

    def insertNode(self, val):
        self.que.append(val)

        newbieIndex = len(self.que) - 1
        while newbieIndex >= 1:
            parentIndex = self.getParentIndex(newbieIndex)
            if parentIndex >= 1 and self.que[newbieIndex] > self.que[parentIndex]:
                self.swap(newbieIndex, parentIndex)
                newbieIndex = parentIndex
            else:
                break

    def swap(self, index1, index2):
        self.que[index2], self.que[index1] = self.que[index1], self.que[index2]

    def getMaxNode(self):
        maxNodeVal = self.que[1]
        self.swap(1, len(self.que)-1)
        self.que.pop()
        self.heapify(1)
        return maxNodeVal

    def heapify(self, index):
        shouldMax = index
        left = self.getLeftChildIndex(index)
        right = self.getRightChildIndex(index)
        if left <= len(self.que) - 1 and self.que[shouldMax] < self.que[left]:
            shouldMax = left
        if right <= len(self.que) - 1 and self.que[shouldMax] < self.que[right]:
            shouldMax = right

        if shouldMax != index:
            self.swap(index, shouldMax)
            self.heapify(shouldMax)

heap = maxHeap()
heap.insertNode(1)
heap.insertNode(2)
heap.insertNode(3)
heap.insertNode(4)
heap.insertNode(5)
heap.insertNode(6)

assert heap.getMaxNode() == 6
assert heap.getMaxNode() == 5
assert heap.getMaxNode() == 4
assert heap.getMaxNode() == 3
assert heap.getMaxNode() == 2
assert heap.getMaxNode() == 1
