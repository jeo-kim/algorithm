import collections
def solution(prices):

    # 준비물
    # (1) 결과로 제출할 배열 answer "[ ] * N" (N = len(prices))
    # (2) 인덱스와 가격을 함께 넣을 main_stack
    # (3) 아직 비교를 기다리고 있는 '대기중인 가격들' (waiting_prices) >> queue

    # 준비물 세팅
    waiting_prices = collections.deque(prices)
    main_stack = [[-1, 0]]  # 첫 값이 stack 에 쌓일 때 비교를 위해 넣어 둔 값.

    answer = [0] * (len(prices))

    # 대기 중인 가격들에 대해서
    for i, price in enumerate(waiting_prices):

        while main_stack[-1][1] > price:  # 만약 지금 메인 스택의 꼭대기(top)의 값보다, 지금 비교하는 가격이 작다면 계속해서.
            top_idx = main_stack.pop()[0]  # stack 꼭대기의 인덱스값과
            days = i - top_idx  # waiting prices 의 맨 앞에 서서 현재 비교 대상이었던 인덱스의 차이를 days 변수로 받아서
            answer[top_idx] = days  # 꼭대기에 있던 아이의 인덱스에 해당하는 answer 칸에 차이를 넣는다.
            # main_stack.pop()  # 그리고 나서 main stack 을 뽑아낸다.

        # 메인 스택의 꼭대기(top)의 값보다, 지금 비교하는 가격이 크거나 같다면
        main_stack.append([i, price])
        # waiting_prices.popleft()


    while len(main_stack) > 1:  # 더 이상 비교해볼 가격은 없고, 메인 스택에 초기화해두었던 [-1, 0] 말고도 남아있다면.
        top_idx = main_stack.pop()[0]
        days = len(prices) - 1 - top_idx
        answer[top_idx] = days

    return answer

prices1= [1, 2, 3, 2, 3]

#[4, 3, 1, 1, 0]

solution(prices1)

