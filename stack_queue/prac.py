from stack_queue.structures import Node, Stack


def test_node():
    assert Node(1, None).item == 1
    # 노드라는 아이의 값을 item 이라는 이름으로 꺼낼 건데 그 값이 1이어야 해.
    # 이걸 만족하는 Node 를 만들기.

def test_stack():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.is_empty()

def test_queue():
    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)

    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 3
    assert queue.pop() == 5
    assert queue.pop() is None
    assert queue.is_empty()

test_node()
test_stack()
test_queue()

