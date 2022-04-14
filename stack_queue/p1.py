# s " []()"
from collections import deque


def is_valid(s) -> bool:
    pair = {
        '}':'{',
        ')':'(',
        ']':'['
    }
    opener = "{[("
    stack = []

    for char in s:
        if char in opener:  # 괄호가 여는 녀석에 해당한다면
            stack.append(char)  # 스택에 넣을 거야.
        else:
            # char 가 닫는 녀석인데, 열었던 애들이 아무도 없어서
            # stack 이 쌓인 게 없다면.
            if not stack:
                return False

            top = stack.pop()  # 꼭대기에 있는 아이를 가져와서
            if pair[top] != top:  # 비교해
                return False

    return not stack

def get_card(num):
    # list?


    queue = deque([n for n in range(1, num+1)])
    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())
    return queue.popleft()





# 스택은 리스트로 써도 되지만,
# 큐는 데크를 쓰는 것이 좋다. 데크는 내부적으로 doubly linked list 이므로.




#
#
# assert is_valid("{}()[]")
# assert is_valid("{[]}")
# assert is_valid("{[()]}")
#
# assert not is_valid("{}]")  # false
# assert not is_valid("{{{{{{{{}}}}}}}")  # false


#########
assert get_card(6) == 4
