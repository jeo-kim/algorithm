import collections
import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())

# 간선 정보들
connect_info = collections.defaultdict(list)
# 결과로 제출할 때 쓸 배열
res = [0] * (n + 1)
# 사용하지 않을 칸을 0이 아닌 값으로 채워두기
res[0] = -1
res[1] = -1

for _ in range(n-1):
    connect = tuple(map(int, sys.stdin.readline().split()))
    connect_info[connect[0]].append(connect[1])
    connect_info[connect[1]].append(connect[0])

def DFS(num):
    if 0 not in res:
        for i in range(2, n+1):
            print(res[i])
        return

    else:
        for child in connect_info[num]:
            if res[child] == 0:
                res[child] = num
                DFS(child)

DFS(1)


