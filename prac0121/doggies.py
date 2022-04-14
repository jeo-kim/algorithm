import sys
from collections import deque

def DFS(L, sum, tsum):
    global result  # 전역변수를 가져와 사용하기 위함.
    if sum + (total-tsum) < result:
    # 앞으로 판단해야 할 친구들을 다 더한다 하더라도 기존의 result 보다 작다면 더 레벨을 내려가면서 확인할 필요가 없다.
        return

    if sum > c:
        return

    if L == 5:
        if sum > result:
            result = sum

    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

if __name__ == "__main__":
    # c, n = map(int, input().split())
    # a = [0]*n
    c = 259
    a = [81, 58, 42, 33, 61]
    result = -2147000000
    total = sum(a)
    DFS(0,0, 0)
    print(result)