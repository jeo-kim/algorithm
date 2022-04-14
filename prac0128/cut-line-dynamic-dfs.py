n = 7

# 메모이제이션을 위한 공간! 이 리스트의 인덱스번호에 해당하는 길이를 몇 가지 방식으로 자를 수 있는지 구하면 거기에 값을 넣어두기.
# 또 다른 곳에서 같은 길이에 대한 재귀적 호출을 하지 않도록 하기 위함.
obtained = [0] * (n+1)

def DFS(length:int):
    # 직관적으로 알 수 있어 미리 정해줄 수 있는 return 값들
    if length == 2:
        return 2
    if length == 1:
        return 1

    else:
        # 이게 이번에 중요하게 배운 포인트! 바로 메모이제이션!
        # 이미 계산한 값이 존재한다면! 초기화해둔 값인 0 이 아닐 것이다.
        # 그렇다면 재귀적 호출 필요 없이 거기서 바로 값을 가져온다.
        if obtained[length] != 0:
            return obtained[length]
        else:
            # 계산한 값이 없다면 하부로 내려가서 구한 값끼리 더해주어야 한다.
            # 그리고 구함과 동시에 그 값을 obtained 에 넣어주어 나중에 같은 계산을 안 하도록 한다.
            obtained[length] = DFS(length-1) + DFS(length-2)
            return obtained[length]

print(DFS(n))