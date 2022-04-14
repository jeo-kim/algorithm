import collections


def which_prince(N:int, K:int) -> int:

    princes = collections.deque()

    for i in range(1, N+1):
        princes.append(i)

    # new_princes = list(range(1, N+1))
    # 이런 식으로 만들 수도 있음.

    while len(princes) > 1:
        for _ in range(K-1):
            princes.append(princes.popleft())
        princes.popleft()

    print(princes)

which_prince(8, 3)