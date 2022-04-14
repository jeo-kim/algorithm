import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

count = 0
def DFS(L, c):  # level, color 를 인자로 사용
    global count
    if L == k:
        count += 1
        return
    # else:
    #     for i in range(c+2, )
    #
    #         81
    #
    #         결석 연속 세번번